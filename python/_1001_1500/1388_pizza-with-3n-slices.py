#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨： 
# 
#  
#  你挑选 任意 一块披萨。 
#  Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。 
#  Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。 
#  重复上述过程直到没有披萨剩下。 
#  
# 
#  每一块披萨的大小按顺时针方向由循环数组 slices 表示。 
# 
#  请你返回你可以获得的披萨大小总和的最大值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：slices = [1,2,3,4,5,6]
# 输出：10
# 解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小
# 为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：slices = [8,9,8,6,1,1]
# 输出：16
# 解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
#  
# 
#  示例 3： 
# 
#  输入：slices = [4,1,2,5,8,3,1,9,7]
# 输出：21
#  
# 
#  示例 4： 
# 
#  输入：slices = [3,1,2]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= slices.length <= 500 
#  slices.length % 3 == 0 
#  1 <= slices[i] <= 1000 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        """
        GOOD TODO
        本题可以转化成如下问题：
             给一个长度为 3n  的环状序列，你可以在其中选择 n 个数，并且任意两个数不能相邻，求这 n 个数的最大值
             dp[i][j] 表示在前 i 个数中选择了 j 个不相邻的数的最大和
             dp[i][j]=max(dp[i−2][j−1]+slices[i],dp[i−1][j])
             环状序列相较于普通序列，相当于添加了一个限制：普通序列中的第一个和最后一个数不能同时选
        """

        def calculate(A):
            N = len(A)
            choose = (N + 1) // 3
            dp = [[0] * (choose + 1) for _ in range(N + 1)]
            for i in range(1, N + 1):
                for j in range(1, choose + 1):
                    if i - 2 >= 0:
                        dp[i][j] = max(dp[i - 1][j], dp[i - 2][j - 1] + A[i-1])
                    else:
                        dp[i][j] = max(dp[i - 1][j], A[i-1])
            return dp[N][choose]

        ans1 = calculate(slices[1:])
        ans2 = calculate(slices[:-1])
        return max(ans1, ans2)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(slices=[1, 2, 3, 4, 5, 6]), 10],
    [dict(slices=[8, 9, 8, 6, 1, 1]), 16],
    [dict(slices=[4, 1, 2, 5, 8, 3, 1, 9, 7]), 21],
    [dict(slices=[3, 1, 2]), 3],
])
def test_solutions(kw, expected):
    assert Solution().maxSizeSlices(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
