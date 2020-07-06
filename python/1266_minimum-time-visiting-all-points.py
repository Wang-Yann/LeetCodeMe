#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。 
# 
#  你可以按照下面的规则在平面上移动： 
# 
#  
#  每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。 
#  必须按照数组中出现的顺序来访问这些点。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：points = [[1,1],[3,4],[-1,0]]
# 输出：7
# 解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> 
# [-1,0]   
# 从 [1,1] 到 [3,4] 需要 3 秒 
# 从 [3,4] 到 [-1,0] 需要 4 秒
# 一共需要 7 秒 
# 
#  示例 2： 
# 
#  输入：points = [[3,2],[-2,2]]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  points.length == n 
#  1 <= n <= 100 
#  points[i].length == 2 
#  -1000 <= points[i][0], points[i][1] <= 1000 
#  
#  Related Topics 几何 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        对于任意一种情况，从 x 移动到 y 的最少次数为 dx 和 dy 中的较大值 max(dx, dy)，这也被称作 x 和 y 之间的 切比雪夫距离
        """
        N = len(points)
        return sum(max(
            abs(points[i + 1][0] - points[i][0]),
            abs(points[i + 1][1] - points[i][1])
        ) for i in range(N - 1))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(points=[[1, 1], [3, 4], [-1, 0]]), 7],
    [dict(points=[[3, 2], [-2, 2]]), 5],
])
def test_solutions(kw, expected):
    assert Solution().minTimeToVisitAllPoints(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
