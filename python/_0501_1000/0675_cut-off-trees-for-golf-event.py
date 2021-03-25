#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你被请来给一个要举办高尔夫比赛的树林砍树. 树林由一个非负的二维数组表示， 在这个数组中： 
# 
#  
#  0 表示障碍，无法触碰到. 
#  1 表示可以行走的地面. 
#  比 1 大的数 表示一颗允许走过的树的高度. 
#  
# 
#  每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。 
# 
#  你被要求按照树的高度从低向高砍掉所有的树，每砍过一颗树，树的高度变为 1 。 
# 
#  你将从（0，0）点开始工作，你应该返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。 
# 
#  可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# 输出: 6
#  
# 
#  示例 2: 
# 
#  输入: 
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# 输出: -1
#  
# 
#  示例 3: 
# 
#  输入: 
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# 输出: 6
# 解释: (0,0) 位置的树，你可以直接砍去，不用算步数
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= forest.length <= 50 
#  1 <= forest[i].length <= 50 
#  0 <= forest[i][j] <= 10^9 
#  
#  Related Topics 广度优先搜索

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    TODO TODO TODO
    https://leetcode-cn.com/problems/cut-off-trees-for-golf-event/solution/wei-gao-er-fu-bi-sai-kan-shu-by-leetcode/
    我们定义距离函数 dist(forest, sr, sc, tr, tc)，该函数计算从源 (sr, sc) 到目标 (tr, tc) 通过障碍物 dist[i][j]==0 的路径距离。（如果路径不可能，此距离函数将返回 -1）


    """

    def cutOffTree(self, forest: List[List[int]]) -> int:
        return self.cutOffTreeFunc(forest, self.bfs)

    def cutOffTreeFunc(self, forest: List[List[int]], dist_func):
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = dist_func(forest, sr, sc, tr, tc)
            if d < 0:
                return -1
            ans += d
            sr, sc = tr, tc
        return ans

    @staticmethod
    def bfs(forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (0 <= nr < R and 0 <= nc < C and
                        (nr, nc) not in seen and forest[nr][nc]):
                    seen.add((nr, nc))
                    queue.append((nr, nc, d + 1))
        return -1

    @staticmethod
    def astar(forest, sr, sc, tr, tc):
        """
        一个 A*搜索是 Dijkstra 的一个特例
        """
        R, C = len(forest), len(forest[0])
        heap = [(0, 0, sr, sc)]
        cost = {(sr, sc):0}
        while heap:
            _cost, dist, r, c = heapq.heappop(heap)
            if r == tr and c == tc:
                return dist
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                    cur_cost = dist + 1 + abs(nr - tr) + abs(nc - tc)
                    if cur_cost < cost.get((nr, nc), 9999):
                        cost[nr, nc] = cur_cost
                        heapq.heappush(heap, (cur_cost, dist + 1, nr, nc))
        return -1

    @staticmethod
    def hadlocks(forest, sr, sc, tr, tc):
        """TODO"""
        R, C = len(forest), len(forest[0])
        processed = set()
        deque = collections.deque([(0, sr, sc)])
        while deque:
            detours, r, c = deque.popleft()
            if (r, c) not in processed:
                processed.add((r, c))
                if r == tr and c == tc:
                    return abs(sr - tr) + abs(sc - tc) + 2 * detours
                for nr, nc, closer in ((r - 1, c, r > tr), (r + 1, c, r < tr),
                                       (r, c - 1, c > tc), (r, c + 1, c < tc)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        if closer:
                            deque.appendleft((detours, nr, nc))
                        else:
                            deque.append((detours + 1, nr, nc))
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([
         [1, 2, 3],
         [0, 0, 4],
         [7, 6, 5]
     ], 6),
    ([
         [1, 2, 3],
         [0, 0, 0],
         [7, 6, 5]
     ], -1),
    ([
         [2, 3, 4],
         [0, 0, 5],
         [8, 7, 6]
     ], 6
    )
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.cutOffTreeFunc(args, sol.bfs) == expected
    assert sol.cutOffTreeFunc(args, sol.astar) == expected
    assert sol.cutOffTreeFunc(args, sol.hadlocks) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
