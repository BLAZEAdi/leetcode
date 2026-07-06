# Templates

Use these whenever you add a new problem. Keeping the format consistent is
what makes the repo easy to skim later (or in an interview when someone asks
you to walk through your GitHub).

## Folder name

```
[difficulty]/[4-digit-number]-[kebab-case-title]/
```

Example: `medium/0002-add-two-numbers/`

## Files per problem

```
0002-add-two-numbers/
├── README.md       # problem statement, approach, complexity
└── solution.py      # (or .js / .java / .cpp) — the actual code
```

## README.md template

```markdown
# [Number]. [Title]

**Difficulty:** Easy | Medium | Hard
**Topics:** Array, Hash Table, ...
**Link:** https://leetcode.com/problems/[slug]/

## Problem

[1-3 sentence restatement of the problem in your own words]

## Approach

[How you solved it — the key insight, not a line-by-line walkthrough]

## Complexity

- Time: O(...)
- Space: O(...)

## Notes

[Anything you'd want future-you to remember: gotchas, a slicker approach you
saw in discuss, why the brute force fails, etc.]
```

## Commit message format

```
[LEETCODE] #[number] [Problem Name] - [Easy|Medium|Hard]

Time: O(...)  Space: O(...)
```

Example:

```
[LEETCODE] #1 Two Sum - Easy

Time: O(n)  Space: O(n)
```

Keeping commit messages consistent makes `git log --oneline` itself read like
a changelog of your progress.
