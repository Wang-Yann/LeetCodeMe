#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 两个玩家分别扮演猫（Cat）和老鼠（Mouse）在无向图上进行游戏，他们轮流行动。 
# 
#  该图按下述规则给出：graph[a] 是所有结点 b 的列表，使得 ab 是图的一条边。 
# 
#  老鼠从结点 1 开始并率先出发，猫从结点 2 开始且随后出发，在结点 0 处有一个洞。 
# 
#  在每个玩家的回合中，他们必须沿着与他们所在位置相吻合的图的一条边移动。例如，如果老鼠位于结点 1，那么它只能移动到 graph[1] 中的（任何）结点去。
#  
# 
#  此外，猫无法移动到洞（结点 0）里。 
# 
#  然后，游戏在出现以下三种情形之一时结束： 
# 
#  
#  如果猫和老鼠占据相同的结点，猫获胜。 
#  如果老鼠躲入洞里，老鼠获胜。 
#  如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局。 
#  
# 
#  给定 graph，并假设两个玩家都以最佳状态参与游戏，如果老鼠获胜，则返回 1；如果猫获胜，则返回 2；如果平局，则返回 0。 
# 
#  
# 
#  
#  
# 
#  示例： 
# 
#  输入：[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# 输出：0
# 解释：
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= graph.length <= 200 
#  保证 graph[1] 非空。 
#  保证 graph[2] 包含非零元素。 
#  
#  Related Topics 广度优先搜索 极小化极大

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
     极大极小
    https://leetcode-cn.com/problems/cat-and-mouse/solution/bu-liao-jie-ji-da-ji-xiao-suan-fa-ke-yi-tong-guo-b/
    """

    def catMouseGame(self, graph: List[List[int]]) -> int:
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3 - t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3 - t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c:  # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    def catMouseGame(self, graph):
        """
        TODO TODO TODO TODO
        错误答案 用例2失败
        """
        HOLE, MOUSE_START, CAT_START = range(3)
        DRAW, MOUSE, CAT = range(3)
        lookup = {}

        def move(i, other_i, is_mouse_turn):
            key = (i, other_i, is_mouse_turn)
            if key in lookup:
                return lookup[key]
            lookup[key] = DRAW
            if is_mouse_turn:
                skip, target, win, lose = other_i, HOLE, MOUSE, CAT
            else:
                skip, target, win, lose = HOLE, other_i, CAT, MOUSE
            for neighbor in graph[i]:
                if neighbor == target:
                    result = win
                    break
            else:
                result = lose
                for neighbor in graph[i]:
                    if neighbor == skip:
                        continue
                    tmp = move(other_i, neighbor, not is_mouse_turn)
                    if tmp == win:
                        result = win
                        break
                    if tmp == DRAW:
                        result = DRAW
            lookup[key] = result
            return result

        return move(MOUSE_START, CAT_START, True)


@pytest.mark.parametrize("args,expected", [
    ([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]], 0),
    ([[6], [4], [9], [5], [1, 5], [3, 4, 6], [0, 5, 10], [8, 9, 10], [7], [2, 7], [6, 7]], 1),
])
def test_solutions(args, expected):
    assert Solution().catMouseGame(args) == expected
    # assert Solution1().catMouseGame(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
