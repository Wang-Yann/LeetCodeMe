#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 10:42:59
# @Last Modified : 2020-07-23 10:42:59
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 图片在计算机处理中往往是使用二维矩阵来表示的。 
# 
#  假设，这里我们用的是一张黑白的图片，那么 0 代表白色像素，1 代表黑色像素。 
# 
#  其中黑色的像素他们相互连接，也就是说，图片中只会有一片连在一块儿的黑色像素（像素点是水平或竖直方向连接的）。 
# 
#  那么，给出某一个黑色像素点 (x, y) 的位置，你是否可以找出包含全部黑色像素的最小矩形（与坐标轴对齐）的面积呢？ 
# 
#  
# 
#  示例: 
# 
#  输入:
# [
#   "0010",
#   "0110",
#   "0100"
# ]
# 和 x = 0, y = 2
# 
# 输出: 6
#  
# 
#  
#  Related Topics 二分查找 
#  👍 10 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        """AC"""
        if not image:
            return 0
        m, n = len(image), len(image[0])
        l = r = t = b = 0
        for i in range(m):
            if "1" in image[i]:
                t = i
                break
        for i in range(m - 1, - 1, -1):
            if "1" in image[i]:
                b = i
                break
        zip_image = list(zip(*image))
        for i in range(n):
            if "1" in zip_image[i]:
                l = i
                break
        for i in range(n - 1, - 1, -1):
            if "1" in zip_image[i]:
                r = i
                break
        return (b - t + 1) * (r - l + 1)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(image=[
        "0010",
        "0110",
        "0100"
    ], x=0, y=2
    ), 6],
])
def test_solutions(kw, expected):
    assert Solution().minArea(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
