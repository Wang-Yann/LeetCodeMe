#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 07:13:03
# @Last Modified : 2021-02-23 07:13:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足： 
# 
#  
#  pairs 中没有重复元素 
#  xi < yi 
#  
# 
#  令 ways 为满足下面条件的有根树的方案数： 
# 
#  
#  树所包含的所有节点值都在 pairs 中。 
#  一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。 
#  注意：构造出来的树不一定是二叉树。 
#  
# 
#  两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。 
# 
#  请你返回： 
# 
#  
#  如果 ways == 0 ，返回 0 。 
#  如果 ways == 1 ，返回 1 。 
#  如果 ways > 1 ，返回 2 。 
#  
# 
#  一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。 
# 
#  我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：pairs = [[1,2],[2,3]]
# 输出：1
# 解释：如上图所示，有且只有一个符合规定的有根树。
#  
# 
#  示例 2： 
# 
#  
# 输入：pairs = [[1,2],[2,3],[1,3]]
# 输出：2
# 解释：有多个符合规定的有根树，其中三个如上图所示。
#  
# 
#  示例 3： 
# 
#  
# 输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
# 输出：0
# 解释：没有符合规定的有根树。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= pairs.length <= 105 
#  1 <= xi < yi <= 500 
#  pairs 中的元素互不相同。 
#  
#  Related Topics 树 图 
#  👍 11 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        """
        TODO
        https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/discuss/1009238/Python-dfs-solution-explained
        HARD
        BORING
        """
        P = pairs
        G = collections.defaultdict(set)
        for u, v in P:
            G[u].add(v)
            G[v].add(u)

        def helper(nodes):
            d, m = collections.defaultdict(list), len(nodes) - 1
            for node in nodes:
                d[len(G[node])].append(node)

            if len(d[m]) == 0:
                return 0
            root = d[m][0]

            for node in G[root]:
                G[node].remove(root)

            comps, seen, i = collections.defaultdict(set), set(), 0

            def dfs(node, i):
                comps[i].add(node)
                seen.add(node)
                for neighbour in G[node]:
                    if neighbour not in seen:
                        dfs(neighbour, i)

            for node in nodes:
                if node != root and node not in seen:
                    dfs(node, i)
                    i += 1

            candidates = [helper(comps[i]) for i in comps]
            if 0 in candidates:
                return 0
            if 2 in candidates:
                return 2
            if len(d[m]) >= 2:
                return 2
            return 1

        return helper(set(G.keys()))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def checkWays(self, pairs: List[List[int]]) -> int:
        """
        https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree/solution/onmde-luan-gao-zuo-fa-by-weak-chicken-y2mv/
        """
        ans = 1
        counter = collections.Counter()
        G = collections.defaultdict(list)
        for u, v in pairs:
            counter[u] += 1
            counter[v] += 1
            G[u].append(v)
            G[v].append(u)
        N = len(counter)
        res = sorted(counter.keys(), key=lambda x: -counter[x])  # 按照关系数排序
        for u, v in pairs:
            if counter[u] == counter[v]:
                ans = 2
        # par[x] 为目前已知的 x 的最近祖先
        parent_map = {}
        if counter[res[0]] != N - 1:  # 判断根的关系数是否满足条件
            ans = 0
        else:
            for i in res:
                parent_map[i] = res[0]  # 将所有节点先挂在根节点下
            flag = True
            vis = {res[0]}
            for i in range(1, N):
                for v in G[res[i]]:
                    if v not in vis:
                        if parent_map[v] != parent_map[res[i]]:  # 判断是否能够更新
                            ans = 0
                            flag = False
                            break
                        parent_map[v] = res[i]  # 将v挂到当前节点res[i]下
                if not flag:
                    break
                vis.add(res[i])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(pairs=[[1, 2], [2, 3]]), 1],
    [dict(pairs=[[1, 2], [2, 3], [1, 3]]), 2],
    [dict(pairs=[[1, 2], [2, 3], [2, 4], [1, 5]]), 0],
])
@pytest.mark.parametrize("SolutionCLS", [Solution1, Solution])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().checkWays(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
