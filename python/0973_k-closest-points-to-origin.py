#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:05:36
# @Last Modified : 2020-05-03 16:05:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import heapq
import traceback
import pytest
from typing import List
import collections, bisect

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x:(x[0]**2+x[1]**2))
        return points[0:K]


class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(point):
            return point[0]**2+point[1]**2
        max_heap = []
        for point in points:
            heapq.heappush(max_heap,(-dist(point),point))
            if len(max_heap)>K:
                heapq.heappop(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(len(max_heap))]

@pytest.mark.parametrize("kwargs,expected", [
    (dict(points = [[1,3],[-2,2]], K = 1), [[-2,2]]),
    pytest.param(dict(points = [[3,3],[5,-1],[-2,4]], K = 2), [[3,3],[-2,4]]),
])
def test_solutions(kwargs, expected):
    assert Solution().kClosest(**kwargs) == expected
    assert sorted(Solution1().kClosest(**kwargs)) == sorted(expected)




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


