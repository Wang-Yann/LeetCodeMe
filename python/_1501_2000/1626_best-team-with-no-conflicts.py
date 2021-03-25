#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 03:08:46
# @Last Modified : 2021-02-25 03:08:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 总和 。 
# 
#  然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 没有矛盾 的球队。如果一名年龄较小球员的分数 严格大于 一名年龄较大的球员，则存在矛盾。同龄球员之间
# 不会发生矛盾。 
# 
#  给你两个列表 scores 和 ages，其中每组 scores[i] 和 ages[i] 表示第 i 名球员的分数和年龄。请你返回 所有可能的无矛盾球队
# 中得分最高那支的分数 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# 输出：34
# 解释：你可以选中所有球员。 
# 
#  示例 2： 
# 
#  输入：scores = [4,5,6,5], ages = [2,1,2,1]
# 输出：16
# 解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。
#  
# 
#  示例 3： 
# 
#  输入：scores = [1,2,3,5], ages = [8,9,10,1]
# 输出：6
# 解释：最佳的选择是前 3 名球员。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= scores.length, ages.length <= 1000 
#  scores.length == ages.length 
#  1 <= scores[i] <= 106 
#  1 <= ages[i] <= 1000 
#  
#  Related Topics 动态规划 
#  👍 32 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """
        GOOD
        longest increasing sequence
        """
        age_socre = sorted([(age, score) for age, score in zip(ages, scores)])
        N = len(age_socre)
        dp = [0] * N

        for i in range(N):
            dp[i] = age_socre[i][1]
            for j in range(i):
                if age_socre[i][1] >= age_socre[j][1]:
                    dp[i] = max(dp[i], age_socre[i][1] + dp[j])
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(scores=[1, 3, 5, 10, 15], ages=[1, 2, 3, 4, 5]), 34],
    [dict(scores=[4, 5, 6, 5], ages=[2, 1, 2, 1]), 16],
    [dict(scores=[1, 2, 3, 5], ages=[8, 9, 10, 1]), 6],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().bestTeamScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
