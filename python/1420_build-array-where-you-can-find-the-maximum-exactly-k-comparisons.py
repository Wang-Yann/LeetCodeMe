#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。 
# 
#  
# 
#  请你生成一个具有下述属性的数组 arr ： 
# 
#  
#  arr 中有 n 个整数。 
#  1 <= arr[i] <= m 其中 (0 <= i < n) 。 
#  将上面提到的算法应用于 arr ，search_cost 的值等于 k 。 
#  
# 
#  返回上述条件下生成数组 arr 的 方法数 ，由于答案可能会很大，所以 必须 对 10^9 + 7 取余。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, m = 3, k = 1
# 输出：6
# 解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
#  
# 
#  示例 2： 
# 
#  输入：n = 5, m = 2, k = 3
# 输出：0
# 解释：没有数组可以满足上述条件
#  
# 
#  示例 3： 
# 
#  输入：n = 9, m = 1, k = 1
# 输出：1
# 解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]
#  
# 
#  示例 4： 
# 
#  输入：n = 50, m = 100, k = 25
# 输出：34549172
# 解释：不要忘了对 1000000007 取余
#  
# 
#  示例 5： 
# 
#  输入：n = 37, m = 17, k = 7
# 输出：418930126
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 50 
#  1 <= m <= 100 
#  0 <= k <= n 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        HARD
        建立动态规划数组dp[n][k+1][m]，其中dp[i][j][p]表示满足如下条件的数组的个数：
            数组长度是i+1
            搜寻代价为j
            数组中最大的数字是p+1
        https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
        solution/jian-dan-san-wei-dong-tai-gui-hua-by-coldme-2/
        """
        if k == 0:
            return 0
        MOD = 10 ** 9 + 7
        dp = [[[0] * m for _ in range(k + 1)] for __ in range(n)]
        dp[0][1] = [1] * m
        for i in range(1, n):
            for j in range(1, k + 1):
                for p in range(m):
                    dp[i][j][p] = sum(dp[i - 1][j - 1][:p]) + dp[i - 1][j][p] * (p + 1)
                    dp[i][j][p] %= MOD
        return sum(dp[n - 1][k]) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=2, m=3, k=1), 6],
    [dict(n=5, m=2, k=3), 0],
    [dict(n=9, m=1, k=1), 1],
    [dict(n=50, m=100, k=25), 34549172],
    [dict(n=37, m=17, k=7), 418930126],
])
def test_solutions(kw, expected):
    assert Solution().numOfArrays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
