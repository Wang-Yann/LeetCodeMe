#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-10-01 23:07:18
# @Last Modified : 2020-10-01 23:07:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `
# y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替
# 换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
# 
# **示例 1：**
# >输入：`leaves = "rrryyyrryyyrr"`
# >
# >输出：`2`
# >
# >解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
# 
# **示例 2：**
# >输入：`leaves = "ryr"`
# >
# >输出：`0`
# >
# >解释：已符合要求，不需要额外操作
# 
# **提示：**
# - `3 <= leaves.length <= 10^5`
# - `leaves` 中只包含字符 `'r'` 和字符 `'y'` 👍 124 👎 0
	 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minimumOperations(self, leaves: str) -> int:
        """
          https://leetcode-cn.com/problems/UlBDOe/solution/dong-tai-gui-hua-python3-by-vzp/
        """
        r, ry, ryr = 1 if leaves[0] == 'y' else 0, float('inf'), float('inf')
        for i in range(1, len(leaves)):
            if leaves[i] == 'r':
                r, ry, ryr = r, min(r, ry) + 1, min(ry, ryr)
            else:
                r, ry, ryr = r + 1, min(r, ry), min(ry, ryr) + 1
        return ryr


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(leaves="rrryyyrryyyrr"), 2],
    pytest.param(dict(leaves="ryr"), 0),
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution,
])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().minimumOperations(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
