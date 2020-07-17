#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 16:05:36
# @Last Modified : 2020-05-03 16:05:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
#
#  （这里，平面上两点之间的距离是欧几里德距离。）
#
#  你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
#
#
#
#  示例 1：
#
#  输入：points = [[1,3],[-2,2]], K = 1
# 输出：[[-2,2]]
# 解释：
# (1, 3) 和原点之间的距离为 sqrt(10)，
# (-2, 2) 和原点之间的距离为 sqrt(8)，
# 由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
# 我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
#
#
#  示例 2：
#
#  输入：points = [[3,3],[5,-1],[-2,4]], K = 2
# 输出：[[3,3],[-2,4]]
# （答案 [[-2,4],[3,3]] 也会被接受。）
#
#
#
#
#  提示：
#
#
#  1 <= K <= points.length <= 10000
#  -10000 < points[i][0] < 10000
#  -10000 < points[i][1] < 10000
#
#  Related Topics 堆 排序 分治算法
#  👍 90 👎 0

"""
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


