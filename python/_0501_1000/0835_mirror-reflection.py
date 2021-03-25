#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 21:52:19
# @Last Modified : 2020-05-05 21:52:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。
#
#  我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。
#
#  （请注意，转换不包括向任何方向旋转。）
#
#  最大可能的重叠是什么？
#
#  示例 1:
#
#  输入：A = [[1,1,0],
#           [0,1,0],
#           [0,1,0]]
#      B = [[0,0,0],
#           [0,1,1],
#           [0,0,1]]
# 输出：3
# 解释: 将 A 向右移动一个单位，然后向下移动一个单位。
#
#  注意:
#
#
#  1 <= A.length = A[0].length = B.length = B[0].length <= 30
#  0 <= A[i][j], B[i][j] <= 1
#
#  Related Topics 数组
#  👍 39 👎 0

"""

import pytest


class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        """
        我们把光线的运动拆分成水平和垂直两个方向来看。在水平和竖直方向，光线都在 0 到 p 之间往返运动，并且水平方向的运动速度是竖直方向的 p/q 倍。
        我们可以将光线的运动抽象成：
            每过一个时间步，光线在水平方向从一侧跳动到另一侧（即移动 p 的距离），同时在竖直方向前进 q 的距离，如果到达了边界就折返


        """
        # targets = [(p, 0), (p, p), (0, p)]
        from fractions import gcd
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2
        if p and q:
            return 1
        else:
            return 0 if p else 2


class Solution1:

    def mirrorReflection(self, p: int, q: int) -> int:
        """
        模拟
        """
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            #Want smallest t so that some x + rx, y + ry is 0 or p
            #x + rxt = 0, then t = -x/rx etc.
            t = float('inf')
            for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            #update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x==y==p else 0 if x==p else 2

@pytest.mark.parametrize("kwargs,expected", [
    (dict(p=2, q=1), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().mirrorReflection(**kwargs) == expected
    assert Solution1().mirrorReflection(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
