#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:38:09
# @Last Modified : 2020-05-04 20:38:09
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。
#
#  每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
#
#
#
#  示例:
#
#  输入: -3, 0, 3, 4, 0, -1, 9, 2
# 输出: 45
#
#  说明: 假设矩形面积不会超出 int 的范围。
#  Related Topics 数学
#  👍 78 👎 0

import pytest


class Solution:

    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (D - B) * (C - A) + (G - E) * (H - F) \
               - max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(F, B))


@pytest.mark.parametrize("args,expected", [
    ([-3, 0, 3, 4, 0, -1, 9, 2], 45),
])
def test_solutions(args, expected):
    assert Solution().computeArea(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
