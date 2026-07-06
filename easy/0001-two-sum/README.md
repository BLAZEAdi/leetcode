# 1. Two Sum

**Difficulty:** Easy
**Topics:** Array, Hash Table
**Link:** https://leetcode.com/problems/two-sum/

## Problem

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`.

You may assume each input has exactly one solution, and you may not use the
same element twice.

## Approach

Use a hash map to store each number's index as we scan the array. For every
element, check whether `target - num` has already been seen. If it has, we
found our pair in a single pass.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Notes

- Brute force is `O(n^2)` (check every pair) — the hash map trick trades space
  for time and is the expected solution in an interview setting.
