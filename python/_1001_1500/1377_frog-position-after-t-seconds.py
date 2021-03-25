#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 22:18:15
# @Last Modified : 2020-07-05 22:18:15
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 n。青蛙从 顶点 1 开始起跳。规则如下： 
# 
#  
#  在一秒内，青蛙从它所在的当前顶点跳到另一个 未访问 过的顶点（如果它们直接相连）。 
#  青蛙无法跳回已经访问过的顶点。 
#  如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。 
#  如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。 
#  
# 
#  无向树的边用数组 edges 描述，其中 edges[i] = [fromi, toi] 意味着存在一条直接连通 fromi 和 toi 两个顶点的边。 
# 
# 
#  返回青蛙在 t 秒后位于目标顶点 target 上的概率。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
# 输出：0.16666666666666666 
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙
# 在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
# 输出：0.3333333333333333
# 解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。 
#  
# 
#  示例 3： 
# 
#  输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
# 输出：0.16666666666666666
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 100 
#  edges.length == n-1 
#  edges[i].length == 2 
#  1 <= edges[i][0], edges[i][1] <= n 
#  1 <= t <= 50 
#  1 <= target <= n 
#  与准确值误差在 10^-5 之内的结果将被判定为正确。 
#  
#  Related Topics 深度优先搜索 
#  👍 18 👎 0

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        G = [[] for _ in range(n + 1)]
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        seen = [0] * (n + 1)

        def dfs(i, t):
            if i != 1 and len(G[i]) == 1 or t == 0:
                return i == target
            seen[i] = 1
            res = sum(dfs(j, t - 1) for j in G[i] if  seen[j]==0)
            return res * 1.0 / (len(G[i]) - (i != 1))

        return dfs(1, t)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        nei = collections.defaultdict(set)
        for a, b in edges:
            nei[a].add(b)
            nei[b].add(a)

        dp = collections.deque([(1, 1, 0)])  # state: leaf_id, possibility, timestamp
        visited = set()

        while dp:
            leaf, p, curr = dp.popleft()
            visited.add(leaf)

            if curr >= t:
                if leaf == target:
                    return p
                continue

            neighbors = nei[leaf] - visited
            for n in neighbors or [leaf]:
                dp += (n, p / (len(neighbors) or 1), curr + 1),
        return 0.0


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=2, target=4), 0.16666666666666666),
    pytest.param(dict(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7), 0.3333333333333333),
    pytest.param(dict(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6), 0.16666666666666666),
])
def test_solutions(kwargs, expected):
    assert Solution().frogPosition(**kwargs) == pytest.approx(expected, 1e-5)
    assert Solution1().frogPosition(**kwargs) == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
