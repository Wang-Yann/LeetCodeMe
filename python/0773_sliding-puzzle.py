#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示. 
# 
#  一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换. 
# 
#  最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。 
# 
#  给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。 
# 
#  示例： 
# 
#  
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#  
# 
#  
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#  
# 
#  
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#  
# 
#  
# 输入：board = [[3,2,4],[1,5,0]]
# 输出：14
#  
# 
#  提示： 
# 
#  
#  board 是一个如上所述的 2 x 3 的数组. 
#  board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列. 
#  
#  Related Topics 广度优先搜索




"""
import collections
import heapq
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    可以把这道题看成一个找出图中最短路径的问题。每个节点都是棋盘的一个状态，如果两个状态之间可以通过一步操作来完成转换，就用一条边将这两个节点相连
    https://leetcode-cn.com/problems/sliding-puzzle/solution/hua-dong-mi-ti-by-leetcode/
    """

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        A*
        """
        M, N = len(board), len(board[0])
        start_board = tuple(itertools.chain(*board))
        pq = [(0, 0, start_board, start_board.index(0))]

        target = tuple(list(range(1, M * N)) + [0])
        target_wrong = tuple(list(range(1, M * N - 2)) + [M * N - 1, M * N - 2, 0])

        cost = {start_board:0}
        expected = {
            (N * r + c + 1) % (M * N):(r, c) for r in range(M) for c in range(N)
        }

        # 预估代价 曼哈顿距离
        def heuristic(board):
            ans = 0
            for r in range(M):
                for c in range(N):
                    val = board[N * r + c]
                    if val == 0:
                        continue
                    er, ec = expected[val]
                    ans += abs(r - er) + abs(c - ec)
            return ans

        # f(n)=g(n)+h(n)
        while pq:
            f, g, board, pos = heapq.heappop(pq)
            if board == target:
                return g
            if board == target_wrong:
                return -1
            if f > cost[board]:
                continue
            for delta in (-1, 1, N, -N):
                neighbor = pos + delta
                if abs(neighbor // N - pos // N) + abs(neighbor % N - pos % N) != 1:
                    continue
                if 0 <= neighbor <= M * N - 1:
                    board2 = list(board)
                    board2[pos], board2[neighbor] = board2[neighbor], board2[pos]
                    board2t = tuple(board2)
                    ncost = g + 1 + heuristic(board2t)
                    if ncost < cost.get(board2t, float("inf")):
                        cost[board2t] = ncost
                        heapq.heappush(pq, (ncost, g + 1, board2t, neighbor))
        return -1


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    可以把这道题看成一个找出图中最短路径的问题。每个节点都是棋盘的一个状态，如果两个状态之间可以通过一步操作来完成转换，就用一条边将这两个节点相连
    """

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """BFS"""
        m, n = len(board), len(board[0])
        start_board = tuple(itertools.chain(*board))
        q = collections.deque([(start_board, start_board.index(0), 0)])
        seen = {start_board}

        target = tuple(list(range(1, m * n)) + [0])
        while q:
            board, pos, depth = q.popleft()
            if board == target:
                return depth
            for direction in (-1, 1, -n, n):
                neighbor = pos + direction
                if abs(neighbor // n - pos // n) + abs(neighbor % n - pos % n) != 1:
                    continue
                if 0 <= neighbor <= m * n - 1:
                    new_board = list(board)
                    new_board[pos], new_board[neighbor] = new_board[neighbor], new_board[pos]
                    newt = tuple(new_board)
                    if newt not in seen:
                        seen.add(newt)
                        q.append((newt, neighbor, depth + 1))
        return -1


@pytest.mark.parametrize("args,expected", [
    ([[1, 2, 3], [4, 0, 5]], 1),
    ([[1, 2, 3], [5, 4, 0]], -1),
    ([[4, 1, 2], [5, 0, 3]], 5),
    ([[3, 2, 4], [1, 5, 0]], 14),
])
def test_solutions(args, expected):
    """
    # BFS模板
    queue = collections.deque([(start, 0)])
    seen = {start}
    while queue:
        node, depth = queue.popleft()
        if node == target: return depth
        for nei in neighbors(node):
            if nei not in seen:
                seen.add(nei)
                queue.append((nei, depth+1))
    """
    assert Solution().slidingPuzzle(args) == expected
    assert Solution1().slidingPuzzle(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
