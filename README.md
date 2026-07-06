# LeetCode Journey 🚀

![Streak](https://img.shields.io/badge/status-actively%20solving-brightgreen)
![Language](https://img.shields.io/badge/language-Python-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

Daily LeetCode practice — solutions, explanations, and complexity notes,
organized by difficulty and topic. This repo is both a public log of my
progress and a personal reference for patterns I've already solved.

## 📊 Progress

<!-- STATS:START -->

**Last updated:** 2026-07-06

| Difficulty | Solved |
|------------|--------|
| 🟢 Easy    | 1 |
| 🟡 Medium  | 0 |
| 🔴 Hard    | 0 |
| **Total**  | **1** |

<!-- STATS:END -->

> This table is auto-updated by [`scripts/update_stats.py`](scripts/update_stats.py)
> every time I push a new solution (see [`.github/workflows/update-stats.yml`](.github/workflows/update-stats.yml)).

See [`PROGRESS_TRACKING.md`](PROGRESS_TRACKING.md) for the full day-by-day log.

## 📁 Structure

Each problem gets its own folder named `[number]-[kebab-case-title]`,
grouped by difficulty:

```
.
├── easy/
│   └── 0001-two-sum/
│       ├── README.md      # problem, approach, complexity
│       └── solution.py
├── medium/
├── hard/
├── scripts/
│   └── update_stats.py    # auto-updates the table above
├── PROGRESS_TRACKING.md    # daily log
└── TEMPLATES.md            # copy-paste templates for new problems
```

## ➕ How I add a new problem

1. Solve it on LeetCode.
2. Create a folder: `[difficulty]/[num]-[kebab-case-title]/`
3. Add `README.md` and `solution.py` (see [`TEMPLATES.md`](TEMPLATES.md) for the format).
4. Add a row to [`PROGRESS_TRACKING.md`](PROGRESS_TRACKING.md).
5. Commit using the format in `TEMPLATES.md`:
   ```
   [LEETCODE] #1 Two Sum - Easy

   Time: O(n)  Space: O(n)
   ```
6. Push — the stats table above updates itself.

I also use [LeetPush](https://github.com/husamql3/leetpush) to auto-capture
accepted solutions from the LeetCode UI straight into this repo, so the
commit-on-solve part stays frictionless.

## 🎯 Goals

- **Weekly:** 5–7 problems
- **Monthly:** 20–30 problems
- **Yearly:** 200+ problems

## 🔗 Resources

- [LeetCode](https://leetcode.com)
- [NeetCode Roadmap](https://neetcode.io/)
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
- [LeetCode Patterns](https://seanprashad.com/leetcode-patterns/)

---

**Started:** July 2026 · **Primary language:** Python
