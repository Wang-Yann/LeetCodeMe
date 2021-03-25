#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。 
# 
#  每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。 
# 
#  您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。 
# 
#  示例 1: 
# 
#  输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  
# 
#  示例 2: 
# 
#  输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#  
# 
#  注意： 
# 
#  
#  cost 的长度将会在 [2, 1000]。 
#  每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。 
#  
#  Related Topics 数组 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        size = len(cost)
        dp = [0] * size
        for i in range(2, size):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        # print(dp)
        return dp[size - 1]


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def minCostClimbingStairs(self, cost):
        dp = [0] * 3
        for i in range(len(cost) - 1, -1, -1):
            dp[i % 3] = cost[i] + min(dp[(i + 1) % 3], dp[(i + 2) % 3])
        return min(dp[0], dp[1])


@pytest.mark.parametrize("args,expected", [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
])
def test_solutions(args, expected):
    assert Solution().minCostClimbingStairs(args) == expected
    assert Solution1().minCostClimbingStairs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
