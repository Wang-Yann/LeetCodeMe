#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-30 23:43:58
# @Last Modified : 2020-04-30 23:43:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
