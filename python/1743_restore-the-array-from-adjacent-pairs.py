#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 14:29:39
# @Last Modified : 2021-02-27 14:29:39
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。 
# 
#  给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui
#  和 vi 在 nums 中相邻。 
# 
#  题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i]
# , nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。 
# 
#  返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：adjacentPairs = [[2,1],[3,4],[3,2]]
# 输出：[1,2,3,4]
# 解释：数组的所有相邻元素对都在 adjacentPairs 中。
# 特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
#  
# 
#  示例 2： 
# 
#  
# 输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
# 输出：[-2,4,1,-3]
# 解释：数组中可能存在负数。
# 另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
#  
# 
#  示例 3： 
# 
#  
# 输入：adjacentPairs = [[100000,-100000]]
# 输出：[100000,-100000]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums.length == n 
#  adjacentPairs.length == n - 1 
#  adjacentPairs[i].length == 2 
#  2 <= n <= 105 
#  -105 <= nums[i], ui, vi <= 105 
#  题目数据保证存在一些以 adjacentPairs 作为元素对的数组 nums 
#  
#  Related Topics 贪心算法 
#  👍 19 👎 0
  

"""

import collections
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        """
        Build the graph in order to locate the ends and access corresponding pairs quickily;
        Traverse the graph built in above 1 and locate an end;
        Staring from the end to find the next element; for each key in the graph, there are at most 2 neighbors in its corresponding values,
            between which one is already found and the other is the next element;
        """
        adj, ans, n = collections.defaultdict(list), [], len(adjacentPairs) + 1
        for a, b in adjacentPairs:
            adj[a] += [b]
            adj[b] += [a]
        prev = -math.inf
        for k, v in adj.items():
            if len(v) == 1:
                ans += [k]
                break
        while len(ans) < n:
            for next in adj.pop(ans[-1]):
                if next != prev:
                    prev = ans[-1]
                    ans += [next]
                    break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(adjacentPairs=[[2, 1], [3, 4], [3, 2]]), [1, 2, 3, 4]],
    [dict(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]), [-2, 4, 1, -3]],
    [dict(adjacentPairs=[[100000, -100000]]), [100000, -100000]],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().restoreArray(**kw)
    adjacentPairs = [sorted(x) for x in kw["adjacentPairs"]]
    for i in range(len(res) - 1):
        assert sorted([res[i], res[i + 1]]) in adjacentPairs


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
