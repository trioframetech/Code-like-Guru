# 🎃 Hacktoberfest LeetCode Solutions 🎃

[![Hacktoberfest 2025](https://img.shields.io/badge/Hacktoberfest-2025-orange.svg)](https://hacktoberfest.digitalocean.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/your-username/leetcode-solutions/issues)
[![GitHub issues](https://img.shields.io/github/issues/your-username/leetcode-solutions.svg)](https://github.com/your-username/leetcode-solutions/issues)
[![GitHub issues closed](https://img.shields.io/github/issues-closed/your-username/leetcode-solutions.svg)](https://github.com/your-username/leetcode-solutions/issues?q=is%3Aissue+is%3Aclosed)

A collection of LeetCode problem solutions for Hacktoberfest 2025. This repository is open to contributions from everyone, especially beginners looking to make their first pull requests during Hacktoberfest!

## 🎯 What is Hacktoberfest?

[Hacktoberfest](https://hacktoberfest.digitalocean.com/) is a month-long celebration of open source software run by DigitalOcean and other sponsors. During the month of October, you're invited to join open-source software enthusiasts, beginners, and the developer community by contributing to open-source projects. Complete the Hacktoberfest challenge and earn a limited edition T-shirt or choose to plant a tree!

## 🚀 How to Contribute

We welcome solutions in any programming language! Here's how to contribute:

1. **Fork this repository** by clicking the Fork button in the top right corner of this page.
2. **Clone your fork** to your local machine:
   ```bash
   git clone https://github.com/your-github-username/leetcode-solutions.git
   cd leetcode-solutions
   ```
3. **Create a new branch** for your solution:
   ```bash
   git checkout -b add-solution/problem-name
   ```
4. **Add your solution** following our folder structure (see below).
5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add solution for Problem XYZ"
   ```
6. **Push to your fork**:
   ```bash
   git push origin add-solution/problem-name
   ```
7. **Create a Pull Request** by navigating to your fork on GitHub and clicking "New Pull Request."

## 📁 Repository Structure

Solutions are organized by difficulty level and numbered according to LeetCode:

```
├── Easy/
│   ├── 0001_two_sum/
│   │   ├── solution.py
│   │   ├── solution.java
│   │   └── README.md (Problem description)
│   └── ...
├── Medium/
│   └── ...
└── Hard/
    ├── 0010_regular_expression_matching/
    │   ├── solution.py
    │   └── README.md (Problem description)
    └── ...
```

## 📝 Solution Template

Each solution file should follow this template:

```python
"""
Problem Name: Regular Expression Matching
Problem URL: https://leetcode.com/problems/regular-expression-matching/
Problem #: 10
Difficulty: Hard

Description:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Time Complexity: O(m*n)
Space Complexity: O(m*n)

@author: Your Name
@date: YYYY-MM-DD
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Your solution here
        pass
```

## 📋 Solutions List

| # | Title | Solution | Difficulty |
|---| ----- | -------- | ---------- |
| 10 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | [Python](./Hard/0010_regular_expression_matching/solution.py) | Hard |

## 🌟 Contribution Guidelines

- Make sure the solution works and passes all LeetCode test cases.
- Include a README.md file with each solution that explains your approach.
- Please add comments to explain your logic, especially for complex solutions.
- Try to optimize your solutions for both time and space complexity.
- If a solution for a particular language already exists, you can add an alternative approach or optimize the existing one.
- Follow good coding practices: proper naming, indentation, and avoid unnecessary code.

## 💻 Supported Languages

We accept solutions in any of these languages (and more!):
- Python
- Java
- C++
- JavaScript
- TypeScript
- Go
- Ruby
- Swift
- Kotlin
- Rust
- C#

## ✅ Hacktoberfest Acceptance Criteria

To qualify for Hacktoberfest:
- Pull requests must be made to a public repository
- PRs should contain commits you made yourself (not automated)
- PRs that are marked as spam or invalid will not count
- PRs must be approved by a maintainer

## 👨‍💻 Top Contributors

Thanks to all the amazing contributors who have helped build this repository!

<a href="https://github.com/your-username/leetcode-solutions/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=your-username/leetcode-solutions" />
</a>

## 📃 License

This repository is licensed under the [MIT License](LICENSE).

## ⭐ Show Your Support

If you find this repository helpful, please give it a ⭐ to show your support!

---

Happy Coding and Happy Hacktoberfest 2025! 🎃
