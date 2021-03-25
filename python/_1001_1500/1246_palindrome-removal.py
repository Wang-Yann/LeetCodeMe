#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-06 17:35:45
# @Last Modified : 2020-08-06 17:35:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr，每一次操作你都可以选择并删除它的一个 回文 子数组 arr[i], arr[i+1], ..., arr[j]（ i <= j）。
#  
# 
#  注意，每当你删除掉一个子数组，右侧元素都会自行向前移动填补空位。 
# 
#  请你计算并返回从数组中删除所有数字所需的最少操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [1,2]
# 输出：2
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,3,4,1,5]
# 输出：3
# 解释：先删除 [4]，然后删除 [1,3,1]，最后再删除 [5]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 100 
#  1 <= arr[i] <= 20 
#  
#  Related Topics 动态规划 
#  👍 33 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        """
        TODO
        区间DP
         dp[i][j]代表i--j的最小次数  两端闭区间
         i 和 j最终消除，则需要满足arr[i] == arr[j]: dp[i][j] = dp[i + 1][j - 1]
        i 和中间某个消除，则最终为dp[i][j] = dp[i][k] + dp[k+1][j]

        """
        N = len(arr)
        dp = [[1] * N for _ in range(N)]
        for gap in range(1, N):
            for i in range(N):
                if i + gap >= N:
                    break
                j = i + gap
                dp[i][j] = float('inf') if arr[i] != arr[j] else dp[i + 1][j - 1]
                for k in range(i, j):
                    # k可以解释为分割位置
                    if arr[i] == arr[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        # print(dp)
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2]), 2],
    [dict(arr=[1, 3, 4, 1, 5]), 3],
])
def test_solutions(kw, expected):
    assert Solution().minimumMoves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
