#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 10:30:21
# @Last Modified : 2021-02-23 10:30:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 n 个节点的树（也就是一个无环连通无向图），节点编号从 0 到 n - 1 ，且恰好有 n - 1 条边，每个节点有一个值。树的 根节点 为 0 
# 号点。 
# 
#  给你一个整数数组 nums 和一个二维数组 edges 来表示这棵树。nums[i] 表示第 i 个点的值，edges[j] = [uj, vj] 表示节
# 点 uj 和节点 vj 在树中有一条边。 
# 
#  当 gcd(x, y) == 1 ，我们称两个数 x 和 y 是 互质的 ，其中 gcd(x, y) 是 x 和 y 的 最大公约数 。 
# 
#  从节点 i 到 根 最短路径上的点都是节点 i 的祖先节点。一个节点 不是 它自己的祖先节点。 
# 
#  请你返回一个大小为 n 的数组 ans ，其中 ans[i]是离节点 i 最近的祖先节点且满足 nums[i] 和 nums[ans[i]] 是 互质的 
# ，如果不存在这样的祖先节点，ans[i] 为 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
# 输出：[-1,0,0,1]
# 解释：上图中，每个节点的值在括号中表示。
# - 节点 0 没有互质祖先。
# - 节点 1 只有一个祖先节点 0 。它们的值是互质的（gcd(2,3) == 1）。
# - 节点 2 有两个祖先节点，分别是节点 1 和节点 0 。节点 1 的值与它的值不是互质的（gcd(3,3) == 3）但节点 0 的值是互质的(gcd(
# 2,3) == 1)，所以节点 0 是最近的符合要求的祖先节点。
# - 节点 3 有两个祖先节点，分别是节点 1 和节点 0 。它与节点 1 互质（gcd(3,2) == 1），所以节点 1 是离它最近的符合要求的祖先节点。
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# 输出：[-1,0,-1,0,0,0,-1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length == n 
#  1 <= nums[i] <= 50 
#  1 <= n <= 105 
#  edges.length == n - 1 
#  edges[j].length == 2 
#  0 <= uj, vj < n 
#  uj != vj 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 数学 
#  👍 4 👎 0

"""

import collections
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ans = [-1] * len(nums)
        path = [[] for _ in range(51)]
        graph = collections.defaultdict(list)
        seen = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, depth):
            if node in seen:
                return
            seen.add(node)
            largestDepth = -1
            for x in range(1, 51):
                if math.gcd(nums[node], x) == 1:
                    # co-prime
                    if len(path[x]) > 0:
                        topNode, topDepth = path[x][-1]
                        if largestDepth < topDepth:
                            # Pick node which has largestDepth and co-prime with current node as our ancestor node
                            largestDepth = topDepth
                            ans[node] = topNode
            path[nums[node]].append((node, depth))
            for nei in graph[node]:
                dfs(nei, depth + 1)
            path[nums[node]].pop()

        dfs(0, 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 3, 3, 2], edges=[[0, 1], [1, 2], [1, 3]]), [-1, 0, 0, 1]],
    [dict(nums=[5, 6, 10, 2, 3, 6, 15], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]),
     [-1, 0, -1, 0, 0, 0, -1]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().getCoprimes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
