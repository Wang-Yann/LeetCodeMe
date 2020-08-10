#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 18:34:49
# @Last Modified : 2020-04-06 18:34:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
#  说明：
#
#
#  所有数字都是正整数。
#  解集不能包含重复的组合。
#
#
#  示例 1:
#
#  输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
#  示例 2:
#
#  输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#  Related Topics 数组 回溯算法
#  👍 137 👎 0

"""

from typing import List

import pytest


class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.helper(result, [], 1, k, n)
        return result

    def helper(self, result: List[List[int]], intermediate: List[int],
               start: int, k: int, target: int) -> None:
        if k == 0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return
        # while start < 10 and start * k + k * (k - 1) / 2 <= target:
        while start < 10:
            intermediate.append(start)
            self.helper(result, intermediate, start + 1, k - 1, target - start)
            intermediate.pop()
            start += 1


@pytest.mark.parametrize("kw,expected", [
    [dict(k=3, n=7), [[1, 2, 4]]],
    [dict(k=3, n=9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]],
])
def test_solutions(kw, expected):
    assert Solution().combinationSum3(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
