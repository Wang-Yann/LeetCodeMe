#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 作为项目经理，你规划了一份需求的技能清单 req_skills，并打算从备选人员名单 people 中选出些人组成一个「必要团队」（ 编号为 i 的备选人员
#  people[i] 含有一份该备选人员掌握的技能列表）。 
# 
#  所谓「必要团队」，就是在这个团队中，对于所需求的技能列表 req_skills 中列出的每项技能，团队中至少有一名成员已经掌握。 
# 
#  我们可以用每个人的编号来表示团队中的成员：例如，团队 team = [0, 1, 3] 表示掌握技能分别为 people[0]，people[1]，和 p
# eople[3] 的备选人员。 
# 
#  请你返回 任一 规模最小的必要团队，团队成员用人员编号表示。你可以按任意顺序返回答案，本题保证答案存在。 
# 
#  
# 
#  示例 1： 
# 
#  输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["
# nodejs","reactjs"]]
# 输出：[0,2]
#  
# 
#  示例 2： 
# 
#  输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people
#  = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp
# ","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= req_skills.length <= 16 
#  1 <= people.length <= 60 
#  1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16 
#  req_skills 和 people[i] 中的元素分别各不相同 
#  req_skills[i][j], people[i][j][k] 都由小写英文字母组成 
#  本题保证「必要团队」一定存在 
#  
#  Related Topics 位运算 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """
        集合覆盖
        """
        N = len(req_skills)
        lookup = dict()
        for i in range(N):
            lookup[req_skills[i]] = i
        dp = [list(range(len(people))) for _ in range(1 << N)]
        dp[0] = []
        for i in range(len(people)):
            # 求这个人的技能
            skill = 0
            for s in people[i]:
                skill |= (1 << lookup[s])
            for k, v in enumerate(dp):
                # 把这个人加入进来以后的团队技能
                new_skills = k | skill
                # 如果团队技能因此而增加 并且增加后的人数比新技能原来的人数少 则更新答案
                if new_skills != k and len(dp[new_skills]) > len(v) + 1:
                    # print(i,k,new_skills,dp[new_skills],v)
                    dp[new_skills] = v + [i]
        # print(dp,lookup)
        return dp[(1 << N) - 1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(req_skills=["java", "nodejs", "reactjs"], people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]), [0, 2]],
    # [dict(req_skills=["algorithms", "math", "java", "reactjs", "csharp", "aws"],
    #       people=[["algorithms", "math", "java"], ["algorithms", "math", "reactjs"],
    #               ["java", "csharp", "aws"], ["reactjs", "csharp"],
    #               ["csharp", "math"], ["aws", "java"]]), [1, 2]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().smallestSufficientTeam(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
