---
description: Temporarily disable the "main protection" ruleset, push current HEAD to main, then re-enable it.
argument-hint: (no args — pushes current HEAD to main)
allowed-tools: Bash(gh api:*), Bash(git push:*), Bash(git log:*), Bash(git branch:*)
---

Push the current branch's `HEAD` straight to `main`, bypassing the GitHub
"main protection" ruleset **for the duration of the push only**. Use this for
typos and other small fixes that don't warrant a PR.

Run the following as a single Bash block, so the ruleset is **always**
re-enabled — even if the push fails:

```bash
set -uo pipefail
REPO="jmuheim/Keymera"

RID=$(gh api "repos/$REPO/rulesets" --jq '.[] | select(.name=="main protection") | .id')
if [ -z "${RID:-}" ]; then
  echo "❌ 'main protection' ruleset not found — aborting, nothing changed."
  exit 1
fi

echo "Branch: $(git branch --show-current)"
echo "Commits that would land on main:"
git log --oneline origin/main..HEAD || true

# Always restore protection, whatever happens next.
restore() {
  if gh api -X PUT "repos/$REPO/rulesets/$RID" -f enforcement=active >/dev/null 2>&1; then
    echo "🔒 main protection re-enabled"
  else
    echo "⚠️  FAILED to re-enable main protection! Run manually:"
    echo "    gh api -X PUT repos/$REPO/rulesets/$RID -f enforcement=active"
  fi
}
trap restore EXIT

gh api -X PUT "repos/$REPO/rulesets/$RID" -f enforcement=disabled >/dev/null && echo "🔓 main protection disabled"
git push origin HEAD:main
```

After it runs, tell me: what was pushed, and confirm protection is `active`
again. If the push was rejected (e.g. non-fast-forward), report the error —
**do not** force-push.
