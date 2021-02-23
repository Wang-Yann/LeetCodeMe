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
        """
        位操作加上dfs 用位存储质因数 temp是一个整形到列表的映射 保存着满足条件的父节点列表
        对于每一个数 枚举所有可能的数字（不到五十个)，如果这个数字和当前数字质因数组成的bitmask没有重叠 则把当前的下标放入temp对应列表
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        possible_combos = set()
        for i in range(1, 51):
            cur = 0
            for j in range(len(primes)):
                if i % primes[j] == 0:
                    cur |= 1 << j
            possible_combos.add(cur)

        N = len(nums)
        connections = collections.defaultdict(set)
        for a, b in edges:
            connections[a].add(b)
            connections[b].add(a)
        ret = [-1] * N

        def visit(idx, temp, prev):
            cur = 0
            for i in range(len(primes)):
                if nums[idx] % primes[i] == 0:
                    cur |= 1 << i
            if temp[cur]:
                ret[idx] = temp[cur][-1]
            for i in possible_combos:
                if i & cur == 0:
                    temp[i].append(idx)
            for b in connections[idx]:
                if b != prev:
                    visit(b, temp, idx)
            for i in possible_combos:
                if i & cur == 0:
                    temp[i].pop()

        visit(0, collections.defaultdict(list), -1)
        return ret


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        stack = collections.defaultdict(list)  # 存储路径上每个值的深度，最后取互质数的最大深度即可
        coprime_map = {key: [x for x in range(1, 51) if math.gcd(x, key) == 1] for key in range(1, 51)}  # 预计算，省很多时间

        # 图有两种选择：
        # 1. 节点*节点: 1/0
        # 2. 节点: [节点]
        # 本题节点量10^5，如果按方式1则要造一个10^10元素的大矩阵，遍历起来极慢
        G = collections.defaultdict(set)
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)

        this_node, path = 0, [0]  # 初始状态
        stack[nums[0]].append(0)
        cnt, e = 0, len(edges)  # BFS计数

        while cnt < e:  # 遍历直到所有边都完成
            if G[this_node]:  # 找到一条可行边
                k = G[this_node].pop()
                G[k].remove(this_node)
                cnt += 1

                _ans = -1  # 寻找该节点的最近互质祖先
                coprimes = coprime_map[nums[k]]  # 遍历预计算好的所有互质数
                for coprime in coprimes:
                    tmp = stack[coprime]
                    if tmp:
                        _ans = max(_ans, tmp[-1])  # 取每个互质数的栈顶
                if _ans != -1:
                    ans[k] = path[_ans]

                path.append(k)  # 更新路径和栈
                stack[nums[k]].append(len(path) - 1)
            else:  # 触及叶子节点，退回父节点
                pop_k = path.pop()  # 路径退栈
                _ = stack[nums[pop_k]].pop()  # 坐标退栈
                k = path[-1]  # 更新栈顶

            this_node = k  # 更新到下一个节点

        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 3, 3, 2], edges=[[0, 1], [1, 2], [1, 3]]), [-1, 0, 0, 1]],
    [dict(nums=[5, 6, 10, 2, 3, 6, 15], edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]),
     [-1, 0, -1, 0, 0, 0, -1]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().getCoprimes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
