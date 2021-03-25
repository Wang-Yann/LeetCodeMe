#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 15:22:55
# @Last Modified : 2020-08-05 15:22:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 colors，里面有 1、2、 3 三种颜色。 
# 
#  我们需要在 colors 上进行一些查询操作 queries，其中每个待查项都由两个整数 i 和 c 组成。 
# 
#  现在请你帮忙设计一个算法，查找从索引 i 到具有目标颜色 c 的元素之间的最短距离。 
# 
#  如果不存在解决方案，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# 输出：[3,0,3]
# 解释： 
# 距离索引 1 最近的颜色 3 位于索引 4（距离为 3）。
# 距离索引 2 最近的颜色 2 就是它自己（距离为 0）。
# 距离索引 6 最近的颜色 1 位于索引 3（距离为 3）。
#  
# 
#  示例 2： 
# 
#  输入：colors = [1,2], queries = [[0,3]]
# 输出：[-1]
# 解释：colors 中没有颜色 3。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= colors.length <= 5*10^4 
#  1 <= colors[i] <= 3 
#  1 <= queries.length <= 5*10^4 
#  queries[i].length == 2 
#  0 <= queries[i][0] < colors.length 
#  1 <= queries[i][1] <= 3 
#  
#  Related Topics 二分查找 
#  👍 10 👎 0

"""

import bisect
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        """AC"""
        lookup = collections.defaultdict(list)
        for i, color in enumerate(colors):
            lookup[color].append(i)
        ans = []
        for pos, c in queries:
            candidates = lookup[c]
            if not candidates:
                ans.append(-1)
                continue
            idx = bisect.bisect_left(candidates, pos)
            if idx == 0:
                ans.append(candidates[0] - pos)
            elif idx == len(candidates):
                ans.append(pos - candidates[-1])
            else:
                ans.append(min(candidates[idx] - pos, pos - candidates[idx - 1]))
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(colors=[1, 1, 2, 1, 3, 2, 2, 3, 3], queries=[[1, 3], [2, 2], [6, 1]]), [3, 0, 3]],
    [dict(colors=[1, 2], queries=[[0, 3]]), [-1]],
])
def test_solutions(kw, expected):
    assert Solution().shortestDistanceColor(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
