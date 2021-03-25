#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 22:06:41
# @Last Modified : 2021-02-26 22:06:41
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个整数数组 source 和 target ，长度都是 n 。还有一个数组 allowedSwaps ，其中每个 allowedSwaps[i] = 
# [ai, bi] 表示你可以交换数组 source 中下标为 ai 和 bi（下标从 0 开始）的两个元素。注意，你可以按 任意 顺序 多次 交换一对特定下标指
# 向的元素。 
# 
#  相同长度的两个数组 source 和 target 间的 汉明距离 是元素不同的下标数量。形式上，其值等于满足 source[i] != target[i
# ] （下标从 0 开始）的下标 i（0 <= i <= n-1）的数量。 
# 
#  在对数组 source 执行 任意 数量的交换操作后，返回 source 和 target 间的 最小汉明距离 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# 输出：1
# 解释：source 可以按下述方式转换：
# - 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
# - 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
# source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
#  
# 
#  示例 2： 
# 
#  输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# 输出：2
# 解释：不能对 source 执行交换操作。
# source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。 
# 
#  示例 3： 
# 
#  输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1
# ,3],[1,4]]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == source.length == target.length 
#  1 <= n <= 105 
#  1 <= source[i], target[i] <= 105 
#  0 <= allowedSwaps.length <= 105 
#  allowedSwaps[i].length == 2 
#  0 <= ai, bi <= n - 1 
#  ai != bi 
#  
#  Related Topics 贪心算法 深度优先搜索 并查集 
#  👍 29 👎 0
  

"""

import collections
import sys
from typing import List

import pytest

sys.setrecursionlimit(10 ** 5)


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        Find each connected part, sum up the common element occurrence.

        """
        res = N = len(source)
        G = [set() for i in range(N)]
        for i, j in allowedSwaps:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * N

        def dfs(pos):
            seen[pos] = 1
            found.append(pos)
            for nei in G[pos]:
                if not seen[nei]:
                    dfs(nei)

        found = []
        for i in range(N):
            if seen[i]:
                continue
            found.clear()
            dfs(i)
            print(i,found)
            counter1 = collections.Counter(source[j] for j in found)
            counter2 = collections.Counter(target[j] for j in found)
            res -= sum((counter1 & counter2).values())
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(source=[1, 2, 3, 4], target=[2, 1, 4, 5], allowedSwaps=[[0, 1], [2, 3]]), 1],
    # [dict(source=[1, 2, 3, 4], target=[1, 3, 2, 4], allowedSwaps=[]), 2],
    # [dict(source=[5, 1, 2, 4, 3], target=[1, 5, 4, 2, 3], allowedSwaps=[[0, 4], [4, 2], [1, 3], [1, 4]]), 0],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minimumHammingDistance(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
