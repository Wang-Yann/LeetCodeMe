#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一个 10^6 x 10^6 的网格中，每个网格块的坐标为 (x, y)，其中 0 <= x, y < 10^6。 
# 
#  我们从源方格 source 开始出发，意图赶往目标方格 target。每次移动，我们都可以走到网格中在四个方向上相邻的方格，只要该方格不在给出的封锁列表 
# blocked 上。 
# 
#  只有在可以通过一系列的移动到达目标方格时才返回 true。否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
#  
# 
#  示例 2： 
# 
#  输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= blocked.length <= 200 
#  blocked[i].length == 2 
#  0 <= blocked[i][j] < 10^6 
#  source.length == target.length == 2 
#  0 <= source[i][j], target[i][j] < 10^6 
#  source != target 
#  
#  Related Topics 广度优先搜索

"""

import sys
from typing import List

import pytest

print("stack limit:", sys.getrecursionlimit())
sys.setrecursionlimit(10 ** 5)


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """

    0th      _________________________
             |O O O O O O O X
             |O O O O O O X
             |O O O O O X
             |O O O O X
             .O O O X
             .O O X
             .O X
    200th    |X

    """

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))

        def dfs(x, y, target, seen):
            if not (0 <= x < 10 ** 6 and 0 <= y < 10 ** 6) or (x, y) in blocked or (x, y) in seen:
                return False
            seen.add((x, y))
            if len(seen) > 20000 or [x, y] == target:
                return True
            return dfs(x + 1, y, target, seen) or \
                   dfs(x - 1, y, target, seen) or \
                   dfs(x, y + 1, target, seen) or \
                   dfs(x, y - 1, target, seen)

        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target:
                            return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000:
                    return True
            return False

        return bfs(source, target) and bfs(target, source)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(blocked=[[0, 1], [1, 0]], source=[0, 0], target=[0, 2]), False),
    pytest.param(dict(blocked=[], source=[0, 0], target=[999999, 999999]), True),
])
def test_solutions(kwargs, expected):
    assert Solution().isEscapePossible(**kwargs) == expected
    # assert Solution1().isEscapePossible(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
