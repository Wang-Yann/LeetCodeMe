#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。 
# 
#  你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上
# 方移动，可以移动的前提是到达的格子没有障碍。 
# 
#  一条路径的 「得分」 定义为：路径上所有数字的和。 
# 
#  请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。 
# 
#  如果没有任何路径可以到达终点，请返回 [0, 0] 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = ["E23","2X2","12S"]
# 输出：[7,1]
#  
# 
#  示例 2： 
# 
#  
# 输入：board = ["E12","1X1","21S"]
# 输出：[4,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：board = ["E11","XXX","11S"]
# 输出：[0,0]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= board.length == board[i].length <= 100 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        rows, cols = len(board), len(board[0])
        dp = [[[0, 0] for _ in range(cols + 1)] for _ in range(rows + 1)]
        MOD = 10 ** 9 + 7

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                curr = board[i - 1][j - 1]
                if curr == 'X':
                    continue
                if curr == 'E':
                    dp[i][j] = [0, 1]
                else:
                    max_dist = max(dp[i - 1][j][0], dp[i][j - 1][0], dp[i - 1][j - 1][0])
                    max_path = 0
                    if dp[i - 1][j][0] == max_dist:
                        max_path += dp[i - 1][j][1]
                        max_path %= MOD
                    if dp[i][j - 1][0] == max_dist:
                        max_path += dp[i][j - 1][1]
                        max_path %= MOD
                    if dp[i - 1][j - 1][0] == max_dist:
                        max_path += dp[i - 1][j - 1][1]
                        max_path %= MOD
                    max_dist += (int(curr) if curr.isdigit() else 0)
                    dp[i][j] = [(max_dist if max_path > 0 else 0), max_path]
        # print(dp)
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            ["E23",
             "2X2",
             "12S"]
            , [7, 1]),
    pytest.param(["E12",
                  "1X1",
                  "21S"], [4, 2]),
    pytest.param(["E11",
                  "XXX",
                  "11S"], [0, 0]),
])
def test_solutions(args, expected):
    assert Solution().pathsWithMaxScore(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
