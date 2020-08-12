#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。 
# 
#  给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。 
# 
#  为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方
# 向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。 
# 
#  最后返回经过上色渲染后的图像。 
# 
#  示例 1: 
# 
#  
# 输入: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 
# 在图像的正中间，(坐标(sr,sc)=(1,1)),
# 在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，
# 因为它不是在上下左右四个方向上与初始点相连的像素点。
#  
# 
#  注意: 
# 
#  
#  image 和 image[0] 的长度在范围 [1, 50] 内。 
#  给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。 
#  image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。 
#  
#  Related Topics 深度优先搜索

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        def dfs(i, j):
            if not (0 <= i <= m - 1 and 0 <= j <= n - 1 and image[i][j] == old_color):
                return
            image[i][j] = newColor
            for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                dfs(i + x, j + y)

        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        dfs(sr, sc)
        return image


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        sr=1, sc=1, newColor=2
    ), [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
])
def test_solutions(kwargs, expected):
    assert Solution().floodFill(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
