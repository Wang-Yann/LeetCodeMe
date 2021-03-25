#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。 
# 
#  你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。 
# 
#  给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。
#  
# 
#  返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：jobDifficulty = [6,5,4,3,2,1], d = 2
# 输出：7
# 解释：第一天，您可以完成前 5 项工作，总难度 = 6.
# 第二天，您可以完成最后一项工作，总难度 = 1.
# 计划表的难度 = 6 + 1 = 7 
#  
# 
#  示例 2： 
# 
#  输入：jobDifficulty = [9,9,9], d = 4
# 输出：-1
# 解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
#  
# 
#  示例 3： 
# 
#  输入：jobDifficulty = [1,1,1], d = 3
# 输出：3
# 解释：工作计划为每天一项工作，总难度为 3 。
#  
# 
#  示例 4： 
# 
#  输入：jobDifficulty = [7,1,7,1,7,1], d = 3
# 输出：15
#  
# 
#  示例 5： 
# 
#  输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# 输出：843
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= jobDifficulty.length <= 300 
#  0 <= jobDifficulty[i] <= 1000 
#  1 <= d <= 10 
#  
#  Related Topics 动态规划

"""
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule/solution/bao-bao-ye-neng-kan-dong-de-leetcode-ti-jie-dfs-1d/
        """
        lj = len(jobDifficulty)
        if lj < d:
            return -1
        dp = [[0x7fffffff] * lj for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, lj):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(i, lj):
                cur_max = jobDifficulty[j]
                for k in range(j, i - 1, -1):
                    cur_max = max(cur_max, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + cur_max)
        return dp[d - 1][lj - 1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        其实就是一个由正整数组成的数组，需要把它分成 d 段，每一段至少有 1 个数字，并且每一段的值为这一段数字中最大的那个数。
        完成分段后便可以计算出所有分段的值的总和，需要返回这个总和的最小值

        """

        @functools.lru_cache(None)
        def dfs(i, d):
            n = len(jobDifficulty)
            if n < d:
                return -1
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res

        return dfs(0, d)


@pytest.mark.parametrize("kw,expected", [
    [dict(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2), 7],
    [dict(jobDifficulty=[9, 9, 9], d=4), -1],
    [dict(jobDifficulty=[1, 1, 1], d=3), 3],
    [dict(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3), 15],
    [dict(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6), 843],
])
def test_solutions(kw, expected):
    assert Solution().minDifficulty(**kw) == expected
    assert Solution1().minDifficulty(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
