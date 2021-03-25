#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:05:59
# @Last Modified : 2020-05-05 16:05:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 假设有 n 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。
#
#  在每一步操作中，你可以选择任意 m （1 ≤ m ≤ n） 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。
#
#  给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的最少的操作步数。如果不能使每台洗衣机中衣物的数量相等，
# 则返回 -1。
#
#
#
#  示例 1：
#
#  输入: [1,0,5]
#
# 输出: 3
#
# 解释:
# 第一步:    1     0 <-- 5    =>    1     1     4
# 第二步:    1 <-- 1 <-- 4    =>    2     1     3
# 第三步:    2     1 <-- 3    =>    2     2     2
#
#
#  示例 2：
#
#  输入: [0,3,0]
#
# 输出: 2
#
# 解释:
# 第一步:    0 <-- 3     0    =>    1     2     0
# 第二步:    1     2 --> 0    =>    1     1     1
#
#
#  示例 3:
#
#  输入: [0,2,0]
#
# 输出: -1
#
# 解释:
# 不可能让所有三个洗衣机同时剩下相同数量的衣物。
#
#
#
#
#  提示：
#
#
#  n 的范围是 [1, 10000]。
#  在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。
#
#
#
#  Related Topics 数学 动态规划
#  👍 41 👎 0

from typing import List

import pytest


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """ 贪心
        https://leetcode-cn.com/problems/super-washing-machines/solution/chao-ji-xi-yi-ji-by-leetcode/
        HARD
        """
        n = len(machines)
        dress_total = sum(machines)
        if dress_total % n != 0:
            return -1

        dress_per_machine = dress_total // n
        for i in range(n):
            # Change the number of dresses in the machines to
            # the number of dresses to be removed from this machine
            # (could be negative)
            machines[i] -= dress_per_machine

        # curr_sum is a number of dresses to move at this point,
        # max_sum is a max number of dresses to move at this point or before,
        # m is number of dresses to move out from the current machine.
        curr_sum = max_sum = res = 0
        for m in machines:
            curr_sum += m
            max_sum = max(max_sum, abs(curr_sum))
            res = max(res, max_sum, m)
        return res


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 5], 3),
    ([0, 3, 0], 2),
    ([0, 2, 0], -1),
])
def test_solutions(args, expected):
    assert Solution().findMinMoves(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
