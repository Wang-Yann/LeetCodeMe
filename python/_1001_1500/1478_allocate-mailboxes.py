#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个房屋数组houses 和一个整数 k ，其中 houses[i] 是第 i 栋房子在一条街上的位置，现需要在这条街上安排 k 个邮筒。 
# 
#  请你返回每栋房子与离它最近的邮筒之间的距离的 最小 总和。 
# 
#  答案保证在 32 位有符号整数范围以内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：houses = [1,4,8,10,20], k = 3
# 输出：5
# 解释：将邮筒分别安放在位置 3， 9 和 20 处。
# 每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：houses = [2,3,5,12,18], k = 2
# 输出：9
# 解释：将邮筒分别安放在位置 3 和 14 处。
# 每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。
#  
# 
#  示例 3： 
# 
#  输入：houses = [7,4,6,1], k = 1
# 输出：8
#  
# 
#  示例 4： 
# 
#  输入：houses = [3,6,14,10], k = 4
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == houses.length 
#  1 <= n <= 100 
#  1 <= houses[i] <= 10^4 
#  1 <= k <= n 
#  数组 houses 中的整数互不相同。 
#  
#  Related Topics 数学 动态规划

"""
import functools
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDistance(self, houses: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/allocate-mailboxes/discuss/685620/JavaC%2B%2BPython-Top-down-DP-Prove-median-mailbox-O(n3)/590468/

        """
        N = len(houses)
        houses = sorted(houses)
        # costs[i][j] is the cost to put a mailbox among houses[i:j], the best way is put the mail box at median position among houses[i:j]
        costs = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])

        @functools.lru_cache(None)
        def dp(k, i):
            if k == 0 and i == N:
                return 0
            if k == 0 or i == N:
                return math.inf
            ans = math.inf
            for j in range(i, N):
                # Try to put a mailbox among house[i:j]
                cost = costs[i][j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def minDistance(self, houses: List[int], k: int) -> int:
        """ https://leetcode.com/problems/allocate-mailboxes/discuss/685403/JavaC%2B%2BPython-DP-Solution"""
        houses.sort()
        n = len(houses)
        prefix = [0]
        for i, a in enumerate(houses):
            prefix.append(prefix[i] + a)

        def cal(i, j):
            m1, m2 = (i + j) // 2, (i + j + 1) // 2
            return (prefix[j + 1] - prefix[m2]) - (prefix[m1 + 1] - prefix[i])

        dp = [cal(0, j) for j in range(n)]
        for k in range(2, k + 1):
            for j in range(n - 1, k - 2, -1):
                for i in range(k - 2, j):
                    dp[j] = min(dp[j], dp[i] + cal(i + 1, j))
        return int(dp[-1])


@pytest.mark.parametrize("kwargs,expected", [
    (dict(houses=[1, 4, 8, 10, 20], k=3), 5),
    pytest.param(dict(houses=[2, 3, 5, 12, 18], k=2), 9),
    pytest.param(dict(houses=[7, 4, 6, 1], k=1), 8),
    pytest.param(dict(houses=[3, 6, 14, 10], k=4), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minDistance(**kwargs) == expected
    assert Solution1().minDistance(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
