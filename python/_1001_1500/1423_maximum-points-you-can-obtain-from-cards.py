#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。 
# 
#  每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。 
# 
#  你的点数就是你拿到手中的所有卡牌的点数之和。 
# 
#  给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：cardPoints = [1,2,3,4,5,6,1], k = 3
# 输出：12
# 解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5
#  = 12 。
#  
# 
#  示例 2： 
# 
#  输入：cardPoints = [2,2,2], k = 2
# 输出：4
# 解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
#  
# 
#  示例 3： 
# 
#  输入：cardPoints = [9,7,7,9,7,7,9], k = 7
# 输出：55
# 解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。
#  
# 
#  示例 4： 
# 
#  输入：cardPoints = [1,1000,1], k = 1
# 输出：1
# 解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 
#  
# 
#  示例 5： 
# 
#  输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
# 输出：202
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= cardPoints.length <= 10^5 
#  1 <= cardPoints[i] <= 10^4 
#  1 <= k <= cardPoints.length 
#  
#  Related Topics 数组 动态规划 Sliding Window

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        dp(l,r) 对应左右拿l,r获取的最大值
        """

        @functools.lru_cache(None)
        def dp(l, r):
            return prefix_sum[-1] - prefix_sum[N - r] + prefix_sum[l]

        N = len(cardPoints)
        prefix_sum = [0]
        for v in cardPoints:
            prefix_sum.append(prefix_sum[-1] + v)
        ans = float("-inf")
        for l in range(k + 1):
            r = k - l
            # print("dp l r",l,r,dp(l,r))
            ans = max(dp(l, r), ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def maxScore(self, cardPoints, k):
        """
       滑动窗口滑中间，思路也很妙
        """
        result, total, curr, left = float("inf"), 0, 0, 0
        for right, point in enumerate(cardPoints):
            total += point
            curr += point
            if right - left + 1 > len(cardPoints) - k:
                curr -= cardPoints[left]
                left += 1
            if right - left + 1 == len(cardPoints) - k:
                result = min(result, curr)
        return total - result


@pytest.mark.parametrize("kw,expected", [
    [dict(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3), 12],
    [dict(cardPoints=[2, 2, 2], k=2), 4],
    [dict(cardPoints=[1, 1000, 1], k=1), 1],
    [dict(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7), 55],
    [dict(cardPoints=[1, 79, 80, 1, 1, 1, 200, 1], k=3), 202],
])
def test_solutions(kw, expected):
    assert Solution().maxScore(**kw) == expected
    assert Solution1().maxScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
