#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。 
# 
#  不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。 
# 
#  现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。 
# 
#  假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, rollMax = [1,1,2,2,2,3]
# 输出：34
# 解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所
# 以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。
#  
# 
#  示例 2： 
# 
#  输入：n = 2, rollMax = [1,1,1,1,1,1]
# 输出：30
#  
# 
#  示例 3： 
# 
#  输入：n = 3, rollMax = [1,1,1,2,2,3]
# 输出：181
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 5000 
#  rollMax.length == 6 
#  1 <= rollMax[i] <= 15 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        """
        
            建立三维数组nums[i][j][cnt]，表示第i次掷出j点且是连续第cnt次掷出了j点。所以最终对nums[-1][j]求和可以得到第n次掷出j点的总的可能数，再让j循环0-5求和
            https://leetcode-cn.com/problems/dice-roll-simulation/solution/pythonhan-jiao-wei-xiang-jin-de-zhu-shi-by-vije/
        """
        MOD = 10 ** 9 + 7
        dp = [[[0 for _ in range(16)] for _ in range(6)] for _ in range(n)]
        for i in range(6):
            dp[0][i][1] = 1  # 第1次掷骰子，点数为i且连续一次
        for i in range(1, n):  # 第i次掷骰子，0-start
            for j in range(6):  # 第i次掷出j点，j=0~5表示1-6点
                for k in range(6):  # 第i-1掷出k点，k=0~5表示1-6点
                    if j != k:  # 若i次与i-1次点数不同，无需考虑重复问题，因为每个数字至少可连续出现一次（rollMax>=1）
                        # 对第i-1次掷出k点的情况，无论是连续的第几次，都求和；此处暗含两次求和，
                        # 一个是数组第三维由sum()求和，另一个是随着k的循环，不断累加得出nums[i][j][1]的值
                        dp[i][j][1] += sum(dp[i - 1][k]) % MOD
                    else:
                        # 若k与j相同，即当前点数与上一次点数相同，则需考察连续次数小于rollMax[j-1]的情况；
                        # 在第i次连续掷出j点m次的序列数等于在第i-1次连续掷出j点m-1次的序列数量。
                        for m in range(2, rollMax[j - 1] + 1):
                            dp[i][j][m] = dp[i - 1][j][m - 1]
        ans = [0, 0, 0, 0, 0, 0]
        # print(dp)
        for j in range(6):
            ans[j] = sum(dp[-1][j]) % MOD
        return sum(ans) % MOD


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=2, rollMax=[1, 1, 2, 2, 2, 3]), 34],
    [dict(n=2, rollMax=[1, 1, 1, 1, 1, 1]), 30],
    [dict(n=3, rollMax=[1, 1, 1, 2, 2, 3]), 181],
])
def test_solutions(kw, expected):
    assert Solution().dieSimulator(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
