#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 22:00:16
# @Last Modified : 2021-02-22 22:00:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。此外，他们还选择了 N 条小路，满足任意两个景点之间都可以通
# 过小路互相到达，且不存在两条连接景点相同的小路。整个游戏场景可视作一个无向连通图，记作二维数组 `edges`，数组中以 `[a,b]` 形式表示景点 a 与景
# 点 b 之间有一条小路连通。
# 
# 小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。游戏开始前，两人分别站在两个不同的景点 `sta
# rtA` 和 `startB`。每一回合，小力先行动，小扣观察到小力的行动后再行动。小力和小扣在每回合可选择以下行动之一：
# - 移动至相邻景点
# - 留在原地
# 
# 如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。
# 
# 注意：小力和小扣一定会采取最优移动策略。
# 
# **示例 1：**
# >输入：`edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5`
# >
# >输出：`3`
# >
# >解释：
# >![image.png](https://pic.leetcode-cn.com/1597991318-goeHHr-image.png){:height
# ="250px"}
# >
# >第一回合，小力移动至 2 号点，小扣观察到小力的行动后移动至 6 号点；
# >第二回合，小力移动至 5 号点，小扣无法移动，留在原地；
# >第三回合，小力移动至 6 号点，小力追到小扣。返回 3。
# 
# 
# **示例 2：**
# >输入：`edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3`
# >
# >输出：`-1`
# >
# >解释：
# >![image.png](https://pic.leetcode-cn.com/1597991157-QfeakF-image.png){:height
# ="250px"}
# >
# >小力如果不动，则小扣也不动；否则小扣移动到小力的对角线位置。这样小力无法追到小扣。
# 
# **提示：**
# - `edges` 的长度等于图中节点个数
# - `3 <= edges.length <= 10^5`
# - `1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]`
# 
# - `1 <= startA, startB <= edges.length 且 startA != startB`
# 
#  👍 10 👎 0
  

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        """
        https://leetcode-cn.com/problems/Za25hA/solution/bfstuo-bu-pai-xu-dfs-by-tom-chan/
        """
        N = max(max(i) for i in edges)
        G = [set() for i in range(N + 1)]
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)

        def bfs(start):
            res = [-1] * (N + 1)
            dq = collections.deque([start])
            res[start] = 0
            while dq:
                p = dq.popleft()
                for i in list(G[p]):
                    if res[i] == -1:
                        res[i] = res[p] + 1
                        dq.append(i)
            return res

        la, lb = bfs(startA), bfs(startB)
        if la[startB] == 1:
            return 1
        res = 1
        for i, j in zip(la, lb):
            if i - j > 1:
                res = max(res, i)
        que = []
        for i in range(1, N + 1):
            if len(G[i]) == 1:
                que.append(i)
        while que:
            x = que.pop()
            for i in list(G[x]):
                G[i].remove(x)
                if len(G[i]) == 1:
                    que.append(i)
            G[x].pop()
        q = []
        for i in range(1, N + 1):
            if len(G[i]) > 1:
                q.append(i)

        def dfs(start, leave, pre, target):
            if leave == 0:
                return True
            for i in G[start]:
                if i == pre:
                    continue
                if i == target:
                    return False
                if not dfs(i, leave - 1, start, target):
                    return False
            return True

        for i in q:
            if la[i] - lb[i] < 2:
                continue
            if dfs(i, 3, -1, i):
                return -1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [2, 5], [5, 6]], startA=3, startB=5), 3],
    pytest.param(dict(edges=[[1, 2], [2, 3], [3, 4], [4, 1]], startA=1, startB=3), -1),
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution,
])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().chaseGame(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
