#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 19:07:26
# @Last Modified : 2020-07-29 19:07:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在 NBA 季后赛中，我们总是安排较强的队伍对战较弱的队伍，例如用排名第 1 的队伍和第 n 的队伍对决，这是一个可以让比赛更加有趣的好策略。现在，给你 n
#  支队伍，你需要以字符串格式输出它们的 最终 比赛配对。 
# 
#  n 支队伍按从 1 到 n 的正整数格式给出，分别代表它们的初始排名（排名 1 最强，排名 n 最弱）。我们用括号（'(', ')'）和逗号（','）来表
# 示匹配对——括号（'(', ')'）表示匹配，逗号（','）来用于分割。 在每一轮的匹配过程中，你都需要遵循将强队与弱队配对的原则。 
# 
#  
# 
#  示例 1： 
# 
#  输入: 2
# 输出: (1,2)
# 解析: 
# 初始地，我们有队1和队2两支队伍，按照1，2排列。
# 因此 用 '(', ')' 和 ','来将队1和队2进行配对，得到最终答案。
#  
# 
#  示例 2： 
# 
#  输入: 4
# 输出: ((1,4),(2,3))
# 解析: 
# 在第一轮，我们将队伍1和4配对，2和3配对，以满足将强队和弱队搭配的效果。得到(1,4),(2,3).
# 在第二轮，(1,4) 和 (2,3) 的赢家需要进行比赛以确定最终赢家，因此需要再在外面加一层括号。
# 于是最终答案是((1,4),(2,3))。
#  
# 
#  示例 3： 
# 
#  输入: 8
# 输出: (((1,8),(4,5)),((2,7),(3,6)))
# 解析: 
# 第一轮: (1,8),(2,7),(3,6),(4,5)
# 第二轮: ((1,8),(4,5)),((2,7),(3,6))
# 第三轮 (((1,8),(4,5)),((2,7),(3,6)))
# 由于第三轮会决出最终胜者，故输出答案为(((1,8),(4,5)),((2,7),(3,6)))。
#  
# 
#  
# 
#  注意: 
# 
#  
#  n 的范围是 [2, 212]. 
#  保证 n 可以写成 2k 的形式，其中 k 是正整数。 
#  
# 
#  
#  Related Topics 递归 字符串 
#  👍 17 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContestMatch(self, n: int) -> str:
        """
        GOOD
        TODO
        """
        matches = list(map(str, range(1, n + 1)))
        while len(matches) // 2:
            matches = ["({},{})".format(matches[i], matches[-i - 1]) for i in range(len(matches) // 2)]
        return matches[0]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def findContestMatch(self, n):
        team = list(map(str, range(1, n + 1)))
        while n > 1:
            for i in range(n // 2):
                team[i] = "({},{})".format(team[i], team.pop())
            n //= 2

        return team[0]


@pytest.mark.parametrize("args,expected", [
    (2, "(1,2)"),
    (4, "((1,4),(2,3))"),
    (8, "(((1,8),(4,5)),((2,7),(3,6)))"),
])
def test_solutions(args, expected):
    assert Solution().findContestMatch(args) == str(expected)
    assert Solution1().findContestMatch(args) == str(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
