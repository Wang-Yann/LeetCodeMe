#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 11:45:23
# @Last Modified : 2020-07-27 11:45:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值： 
# 
#  
#  -1 表示墙或是障碍物 
#  0 表示一扇门 
#  INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 
# 的。 
#  
# 
#  你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。 
# 
#  示例： 
# 
#  给定二维网格： 
# 
#  INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
#  
# 
#  运行完你的函数后，该网格应该变成： 
# 
#    3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
#  
#  Related Topics 广度优先搜索 
#  👍 62 👎 0

"""

import collections
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
INF = 2147483647


class Solution:
    """AC"""

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        R, C = len(rooms), len(rooms[0])
        dq = collections.deque()
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == 0:
                    dq.append((i, j))
        dis = 1
        while dq:
            l = len(dq)
            for _ in range(l):
                i, j = dq.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i + x, j + y
                    if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and rooms[nx][ny] == INF:
                        rooms[nx][ny] = dis
                        dq.append((nx, ny))
            dis += 1


# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],

    ]

    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
    Solution().wallsAndGates(rooms)
    # print(rooms)
    assert rooms == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
