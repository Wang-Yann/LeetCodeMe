#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 01:14:52
# @Last Modified : 2020-07-06 01:14:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]
#  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。 
# 
#  在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。 
# 
#  请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# 输出：3 
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# 输出：4 
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
#  
# 
#  示例 3： 
# 
#  输入：n = 11, dependencies = [], k = 2
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 15 
#  1 <= k <= n 
#  0 <= dependencies.length <= n * (n-1) / 2 
#  dependencies[i].length == 2 
#  1 <= xi, yi <= n 
#  xi != yi 
#  所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。 
#  题目输入的图是个有向无环图。 
#  
#  Related Topics 图 
#  👍 20 👎 0

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        """
        TODO TODO
        # Time:  O((n * C(c, min(c, k))) * 2^n)
        # Space: O(2^n)
        旅行商问题 NP
        所有的贪心算法都是错的

        """
        reqs = [0] * n
        # 状态压缩 + 深度优先搜索
        for u, v in dependencies:
            reqs[v - 1] |= 1 << (u - 1)
        # print("reqs", reqs)
        dp = [n] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            candidates = []
            for v in range(n):
                if (mask & (1 << v)) == 0 and (mask & reqs[v]) == reqs[v]:
                    candidates.append(v)
            for choice in itertools.combinations(candidates, min(len(candidates), k)):
                new_mask = mask
                for v in choice:
                    new_mask |= 1 << v
                dp[new_mask] = min(dp[new_mask], dp[mask] + 1)
        # print("reqs", reqs, "dp", dp)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    # (dict(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2), 3),
    # pytest.param(dict(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2), 4),
    # pytest.param(dict(n=11, dependencies=[], k=2), 6),
    pytest.param(dict(n=9, dependencies=[[1, 4], [1, 5], [3, 5], [3, 6], [2, 6], [2, 7], [8, 4], [8, 5], [9, 6], [9, 7]], k=3), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().minNumberOfSemesters(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
