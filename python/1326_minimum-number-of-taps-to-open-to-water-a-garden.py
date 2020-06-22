#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在 x 轴上有一个一维的花园。花园长度为 n，从点 0 开始，到点 n 结束。 
# 
#  花园里总共有 n + 1 个水龙头，分别位于 [0, 1, ..., n] 。 
# 
#  给你一个整数 n 和一个长度为 n + 1 的整数数组 ranges ，其中 ranges[i] （下标从 0 开始）表示：如果打开点 i 处的水龙头，可
# 以灌溉的区域为 [i - ranges[i], i + ranges[i]] 。 
# 
#  请你返回可以灌溉整个花园的 最少水龙头数目 。如果花园始终存在无法灌溉到的地方，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 5, ranges = [3,4,1,1,0,0]
# 输出：1
# 解释：
# 点 0 处的水龙头可以灌溉区间 [-3,3]
# 点 1 处的水龙头可以灌溉区间 [-3,5]
# 点 2 处的水龙头可以灌溉区间 [1,3]
# 点 3 处的水龙头可以灌溉区间 [2,4]
# 点 4 处的水龙头可以灌溉区间 [4,4]
# 点 5 处的水龙头可以灌溉区间 [5,5]
# 只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
#  
# 
#  示例 2： 
# 
#  输入：n = 3, ranges = [0,0,0,0]
# 输出：-1
# 解释：即使打开所有水龙头，你也无法灌溉整个花园。
#  
# 
#  示例 3： 
# 
#  输入：n = 7, ranges = [1,2,1,0,2,1,0,1]
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：n = 8, ranges = [4,0,0,0,0,0,0,0,4]
# 输出：2
#  
# 
#  示例 5： 
# 
#  输入：n = 8, ranges = [4,0,0,0,4,0,0,0,4]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^4 
#  ranges.length == n + 1 
#  0 <= ranges[i] <= 100 
#  
#  Related Topics 贪心算法 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        def jump_game(A):
            cnt, reachable, cur_reachable = 0, 0, 0
            for i, length in enumerate(A):
                if i > reachable:
                    return -1
                if i > cur_reachable:
                    cur_reachable = reachable
                    cnt += 1
                reachable = max(reachable, i + length)
            return cnt

        max_range = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left, right = max(i - r, 0), min(i + r, n)
            max_range[left] = max(max_range[left], right - left)
        # print("max_range",max_range)
        return jump_game(max_range)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        prev = list(range(n + 1))
        for i in range(n + 1):
            l = max(i - ranges[i], 0)
            r = min(i + ranges[i], n)
            prev[r] = min(prev[r], l)
        BIG = 0x7fffffff
        # print(prev)
        dp = [0] + [BIG] * n
        for i in range(1, n + 1):
            for j in range(prev[i], i):
                if dp[j] != BIG:
                    dp[i] = min(dp[i], dp[j] + 1)
        return -1 if dp[n] == BIG else dp[n]


@pytest.mark.parametrize("kw,expected", [
    [dict(n=5, ranges=[3, 4, 1, 1, 0, 0]), 1],
    [dict(n=3, ranges=[0, 0, 0, 0]), -1],
    [dict(n=7, ranges=[1, 2, 1, 0, 2, 1, 0, 1]), 3],
    [dict(n=8, ranges=[4, 0, 0, 0, 0, 0, 0, 0, 4]), 2],
    [dict(n=8, ranges=[4, 0, 0, 0, 4, 0, 0, 0, 4]), 1],
])
def test_solutions(kw, expected):
    assert Solution().minTaps(**kw) == expected
    assert Solution1().minTaps(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
