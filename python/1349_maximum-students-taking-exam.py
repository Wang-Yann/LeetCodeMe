#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 m * n 的矩阵 seats 表示教室中的座位分布。如果座位是坏的（不可用），就用 '#' 表示；否则，用 '.' 表示。 
# 
#  学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试
# 且无法作弊的最大学生人数。 
# 
#  学生必须坐在状况良好的座位上。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：seats = [["#",".","#","#",".","#"],
#              [".","#","#","#","#","."],
#              ["#",".","#","#",".","#"]]
# 输出：4
# 解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 
#  
# 
#  示例 2： 
# 
#  输入：seats = [[".","#"],
#              ["#","#"],
#              ["#","."],
#              ["#","#"],
#              [".","#"]]
# 输出：3
# 解释：让所有学生坐在可用的座位上。
#  
# 
#  示例 3： 
# 
#  输入：seats = [["#",".",".",".","#"],
#              [".","#",".","#","."],
#              [".",".","#",".","."],
#              [".","#",".","#","."],
#              ["#",".",".",".","#"]]
# 输出：10
# 解释：让学生坐在第 1、3 和 5 列的可用座位上。
#  
# 
#  
# 
#  提示： 
# 
#  
#  seats 只包含字符 '.' 和'#' 
#  m == seats.length 
#  n == seats[i].length 
#  1 <= m <= 8 
#  1 <= n <= 8 
#  
#  Related Topics 动态规划

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        """
        https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/xiang-jie-ya-suo-zhuang-tai-dong-tai-gui-hua-jie-f/
        状压DP
        dp[i][j] 表示当第 i 行的座位分布为 j 时，前 i 行可容纳的最大学生人数
        """
        m, n = len(seats), len(seats[0])
        dp = [[0] * (1 << n) for _ in range(m + 1)]
        # 将 # 设为 1，当遇到 . 时与运算结果为 0，表示可以坐人
        a = [functools.reduce(lambda x, y: x | 1 << y,
                              [0] + [j for j in range(n) if seats[i][j] == '#'])
             for i in range(m)]
        # print([bin(x) for x in a], a)
        for row in range(m - 1, -1, -1):  # 倒着遍历
            for j in range(1 << n):
                # j & a[row]代表该位置可以坐人，j & j<<1 and not j&j>>1 表示该位置左右没人可以坐的
                if not j & (j << 1) and not j & (j >> 1) and not j & a[row]:
                    for k in range(1 << n):
                        # j状态的左上和右上没有人
                        if not j & (k << 1) and not j & (k >> 1):
                            dp[row][j] = max(dp[row][j], dp[row + 1][k] + bin(j).count('1'))
        # print(dp)
        return max(dp[0])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(seats=[["#", ".", "#", "#", ".", "#"],
                 [".", "#", "#", "#", "#", "."],
                 ["#", ".", "#", "#", ".", "#"]]
          ), 4],
    [dict(seats=[[".", "#"],
                 ["#", "#"],
                 ["#", "."],
                 ["#", "#"],
                 [".", "#"]]
          ), 3],
    [dict(seats=[["#", ".", ".", ".", "#"],
                 [".", "#", ".", "#", "."],
                 [".", ".", "#", ".", "."],
                 [".", "#", ".", "#", "."],
                 ["#", ".", ".", ".", "#"]]
          ), 10],

])
def test_solutions(kw, expected):
    assert Solution().maxStudents(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
