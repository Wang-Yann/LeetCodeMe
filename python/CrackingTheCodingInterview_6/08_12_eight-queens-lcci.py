#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:57:03
# @Last Modified : 2020-07-13 11:57:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 回溯算法 
#  👍 26 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        st = [['.' for i in range(n)] for j in range(n)]
        res = []

        def dfs(x_d, y_d, cur):
            j = len(cur)
            if len(cur) == n:
                m = []
                for i in st:
                    m.append(''.join(i))
                res.append(m)
            for i in range(n):
                if i not in cur and i + j not in x_d and i - j not in y_d:
                    st[j][i] = 'Q'
                    dfs(x_d + [i + j], y_d + [i - j], cur + [i])
                    st[j][i] = '.'

        dfs([], [], [])
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
])
def test_solutions(args, expected):
    assert sorted(Solution().solveNQueens(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
