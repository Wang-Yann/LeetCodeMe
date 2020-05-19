#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法

"""
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(begin, path):
            if len(path) == k:
                ans.append(path[:])
            for i in range(begin, n+1):
                path.append(i)
                backtrack(i+1, path)
                path.pop()
        backtrack(1, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def combine(self, n: int, k: int) -> List[List[int]]:
        return [sorted(x) for x in itertools.combinations(list(range(1, n + 1)), k)]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=4, k=2), [[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4], ]),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().combine(**kwargs)) == sorted(expected)
    assert sorted(Solution1().combine(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
