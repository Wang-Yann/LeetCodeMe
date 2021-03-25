#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 03:46:37
# @Last Modified : 2021-02-25 03:46:37
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你 n 个二维平面上的点 points ，其中 points[i] = [xi, yi] ，请你返回两点之间内部不包含任何点的 最宽垂直面积 的宽度。 
# 
#  垂直面积 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 最宽垂直面积 为宽度最大的一个垂直面积。 
# 
#  请注意，垂直区域 边上 的点 不在 区域内。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：points = [[8,7],[9,9],[7,4],[9,7]]
# 输出：1
# 解释：红色区域和蓝色区域都是最优区域。
#  
# 
#  示例 2： 
# 
#  
# 输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == points.length 
#  2 <= n <= 105 
#  points[i].length == 2 
#  0 <= xi, yi <= 109 
#  
#  Related Topics 排序 
#  👍 8 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = sorted(set(x[0] for x in points))
        ans = 0
        for l, r in zip(xs, xs[1:]):
            ans = max(ans, r - l)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(points=[[8, 7], [9, 9], [7, 4], [9, 7]]), 1],
    [dict(points=[[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]), 3],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxWidthOfVerticalArea(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
