#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个二维网格 grid。 "." 代表一个空房间， "#" 代表一堵墙， "@" 是起点，（"a", "b", ...）代表钥匙，（"A", "B", 
# ...）代表锁。 
# 
#  我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们
# 手里有对应的钥匙，否则无法通过锁。 
# 
#  假设 K 为钥匙/锁的个数，且满足 1 <= K <= 6，字母表中的前 K 个字母在网格中都有自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应
# 的钥匙，每个钥匙也有唯一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。 
# 
#  返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["@.a.#","###.#","b.A.B"]
# 输出：8
#  
# 
#  示例 2： 
# 
#  输入：["@..aA","..B#.","....b"]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 30 
#  1 <= grid[0].length <= 30 
#  grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F' 
#  钥匙的数目范围是 [1, 6]，每个钥匙都对应一个不同的字母，正好打开一个对应的锁。 
#  
#  Related Topics 堆 广度优先搜索

"""
import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        GOOD TODO
        jiuzhang
        """
        POSSIBLE_KEYS = "abcdef"
        R, C = len(grid), len(grid[0])
        num_of_keys = 0
        direct = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        moves = set()
        start_i, start_j = 0, 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "@":
                    start_i, start_j = i, j
                elif grid[i][j] in POSSIBLE_KEYS:
                    num_of_keys += 1
        deque = collections.deque()
        deque.append([start_i, start_j, 0, ".@abcdef", 0])
        while deque:
            i, j, steps, keys, collected_keys = deque.popleft()
            if grid[i][j] in POSSIBLE_KEYS and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collected_keys += 1
            if collected_keys == num_of_keys:
                return steps

            for x, y in direct:
                ni, nj = i + x, j + y
                if 0 <= ni <= R - 1 and 0 <= nj <= C - 1 and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in moves:
                        moves.add((ni, nj, keys))
                        deque.append([ni, nj, steps + 1, keys, collected_keys])
        return -1


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """
        官方
        关键点 + Dijkstra

        https://leetcode-cn.com/problems/shortest-path-to-get-all-keys/solution/huo-qu-suo-you-yao-chi-de-zui-duan-lu-jing-by-leet/
        """

        R, C = len(grid), len(grid[0])
        location = {v:(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v not in ".#"}

        def neighbors(r, c):
            for x, y in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r + x, c + y
                if 0 <= nr <= R - 1 and 0 <= nc <= C - 1:
                    yield nr, nc

        def bfs_from(source):
            r, c = location[source]
            seen = [[False] * C for _ in range(R)]
            seen[r][c] = True
            queue = collections.deque([(r, c, 0)])
            dist = {}
            while queue:
                r, c, d = queue.popleft()
                if source != grid[r][c] != ".":
                    dist[grid[r][c]] = d
                    continue
                for nr, nc in neighbors(r, c):
                    if grid[nr][nc] != "#" and not seen[nr][nc]:
                        seen[nr][nc] = True
                        queue.append((nr, nc, d + 1))
            return dist

        dists = {place:bfs_from(place) for place in location}
        target_state = 2 ** sum(p.islower() for p in location) - 1

        # Dijkstra
        pq = [(0, '@', 0)]
        final_dist = collections.defaultdict(lambda:float('inf'))
        final_dist['@', 0] = 0

        while pq:
            d, place, state = heapq.heappop(pq)
            if final_dist[place, state] < d:
                continue
            if state == target_state:
                return d
            for dest, d2 in dists[place].items():
                state2 = state
                # key
                if dest.islower():
                    state2 |= (1 << (ord(dest) - ord("a")))
                    # lock
                elif dest.isupper():
                    # no key
                    if not (state & (1 << (ord(dest) - ord("A")))):
                        continue
                if d + d2 < final_dist[dest, state2]:
                    final_dist[dest, state2] = d + d2
                    heapq.heappush(pq, (d + d2, dest, state2))
        return -1


@pytest.mark.parametrize("args,expected", [
    (["@.a.#", "###.#", "b.A.B"], 8),
    pytest.param(["@..aA", "..B#.", "....b"], 6),
])
def test_solutions(args, expected):
    assert Solution().shortestPathAllKeys(args) == expected
    assert Solution1().shortestPathAllKeys(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
