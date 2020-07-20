#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 23:43:58
# @Last Modified : 2020-04-30 23:43:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果
# 一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
#  [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
#  但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
#
#
#  示例 1：
#
#  输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "A
# BCCED"
# 输出：true
#
#
#  示例 2：
#
#  输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
#
#  提示：
#
#
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#
#
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
#  Related Topics 动态规划
#  👍 115 👎 0

from typing import List

import pytest


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:return False
        if not word:return True
        m,n = len(board),len(board[0])

        def need_walk_pos(i,j,visited):
            return 0<=i<=m-1 and 0<=j<=n-1 and (i,j) not in visited

        def dfs(pos_x,pox_y,curr,visited,k):
            if curr == word:
                return True
            for x,y in [
                (pos_x,pox_y-1),(pos_x,pox_y+1),
                (pos_x-1,pox_y),(pos_x+1,pox_y)]:
                if need_walk_pos(x,y,visited) and board[x][y]==word[k+1]:
                    visited.append((x,y))
                    if dfs(x,y,curr+board[x][y],visited,k+1):
                        return True
                    visited.pop()
        for i in range(m):
            for j in range(n):
                if board[i][j]!=word[0]:
                    continue
                res = dfs(i,j,word[0],[(i,j)],0)
                if res:
                    return True
        return False


@pytest.mark.parametrize("kwargs,expected", [
    (dict(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
          word="ABCCED"), True),
    pytest.param(dict(board=[["a", "b"], ["c", "d"]], word="abcd"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().exist(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
