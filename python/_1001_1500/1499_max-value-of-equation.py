#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 01:25:12
# @Last Modified : 2020-07-06 01:25:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个数组 points 和一个整数 k 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 points[i] =
#  [xi, yi] ，并且在 1 <= i < j <= points.length 的前提下， xi < xj 总成立。 
# 
#  请你找出 yi + yj + |xi - xj| 的 最大值，其中 |xi - xj| <= k 且 1 <= i < j <= points.lengt
# h。 
# 
#  题目测试数据保证至少存在一对能够满足 |xi - xj| <= k 的点。 
# 
#  
# 
#  示例 1： 
# 
#  输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# 输出：4
# 解释：前两个点满足 |xi - xj| <= 1 ，带入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 1
# 0 + -10 + |5 - 6| = 1 。
# 没有其他满足条件的点，所以返回 4 和 1 中最大的那个。 
# 
#  示例 2： 
# 
#  输入：points = [[0,0],[3,0],[9,2]], k = 3
# 输出：3
# 解释：只有前两个点满足 |xi - xj| <= 3 ，带入方程后得到值 0 + 0 + |0 - 3| = 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= points.length <= 10^5 
#  points[i].length == 2 
#  -10^8 <= points[i][0], points[i][1] <= 10^8 
#  0 <= k <= 2 * 10^8 
#  对于所有的1 <= i < j <= points.length ，points[i][0] < points[j][0] 都成立。也就是说，xi 是严格
# 递增的。 
#  
#  Related Topics 数组 Sliding Window 
#  👍 7 👎 0

"""

import collections
import heapq
import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
        Good

         Priority Queue

        because xi < xj,
        yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

        So we only need to find out the maximum yi - xi.
        To find out the maximum element in a sliding window,
        we can use priority queue or stack.
        # xi < xj 总成立
        """
        # 最大堆
        pq = []
        res = -math.inf
        for x, y in points:
            while pq and pq[0][1] < x - k:
                heapq.heappop(pq)
            if pq:
                res = max(res, - pq[0][0]+ x + y )
            heapq.heappush(pq, (x - y, x))
            # print(pq)
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        """
       Time O(N)
        Space O(N)
        """
        dq = collections.deque()
        res = -math.inf
        for x, y in points:
            while dq and dq[0][1] < x - k:
                dq.popleft()
            if dq:
                res = max(res, x + y + dq[0][0])
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append([y - x, x])
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1), 4),
    pytest.param(dict(points=[[0, 0], [3, 0], [9, 2]], k=3), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().findMaxValueOfEquation(**kwargs) == expected
    assert Solution1().findMaxValueOfEquation(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
