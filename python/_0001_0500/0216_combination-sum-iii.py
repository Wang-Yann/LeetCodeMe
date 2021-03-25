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
        def dfs(path, start, cur_k, cur_target):
            if cur_k == 0 and cur_target == 0:
                result.append(list(path))
                return
            elif cur_k < 0:
                return
            # while start < 10 and start * k + k * (k - 1) / 2 <= target:
            while start < 10:
                path.append(start)
                dfs(path, start + 1, cur_k - 1, cur_target - start)
                path.pop()
                start += 1

        result = []
        dfs([], 1, k, n)
        return result


class Solution1:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start, path, cur_size, cur_target):
            if cur_size > k or cur_size + N - start + 1 < k:
                return
            if cur_size == k and cur_target == 0:
                result.append(path[:])
                return
            path.append(start)
            dfs(start + 1, path, cur_size + 1, cur_target - start)
            path.pop()
            dfs(start + 1, path, cur_size, cur_target)

        N = 9
        result = []
        dfs(1, [], 0, n)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(k=3, n=7), [[1, 2, 4]]],
    [dict(k=3, n=9), [[1, 2, 6], [1, 3, 5], [2, 3, 4]]],
    [dict(k=2, n=18), []],
])
def test_solutions(kw, expected):
    assert Solution().combinationSum3(**kw) == expected
    assert Solution1().combinationSum3(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
