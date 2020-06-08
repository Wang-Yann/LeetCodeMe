#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能
# 围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# 输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
# 解释:
# 
#  
# 
#  示例 2: 
# 
#  输入: [[1,2],[2,2],[4,2]]
# 输出: [[1,2],[2,2],[4,2]]
# 解释:
# 
# 即使树都在一条直线上，你也需要先用绳子包围它们。
#  
# 
#  
# 
#  注意: 
# 
#  
#  所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。 
#  输入的整数在 0 到 100 之间。 
#  花园至少有一棵树。 
#  所有树的坐标都是不同的。 
#  输入的点没有顺序。输出顺序也没有要求。 
#  Related Topics 几何

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """
        凸包的模板题,通常使用 Graham扫描法和安德鲁算法,采用安德鲁算法
        https://www.cnblogs.com/l1l1/p/9432876.html
        """
        points = sorted(points)
        if len(points) <= 1:
            return points

        def cross_product(origin, pnt_a, pnt_b):
            return (pnt_a[0] - origin[0]) * (pnt_b[1] - origin[1]) - (pnt_a[1] - origin[1]) * (pnt_b[0] - origin[0])

        lower = []
        for p in points:
            while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(tuple(p))
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(tuple(p))
        # 首位相接且第一个点重复两次
        # print(lower,upper)
        # [(1, 1), (2, 0), (4, 2)] [(4, 2), (3, 3), (2, 4), (1, 1)]
        return [list(p) for p in set(lower[:-1]) | set(upper[:-1])]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
     [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4]]),
    ([[1, 2], [2, 2], [4, 2]],
     [[1, 2], [2, 2], [4, 2]])
])
def test_solutions(args, expected):
    assert sorted(Solution().outerTrees(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
