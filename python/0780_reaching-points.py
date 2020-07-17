#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:59:08
# @Last Modified : 2020-05-05 18:59:08
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 从点 (x, y) 可以转换到 (x, x+y) 或者 (x+y, y)。
#
#  给定一个起点 (sx, sy) 和一个终点 (tx, ty)，如果通过一系列的转换可以从起点到达终点，则返回 True ，否则返回 False。
#
#
# 示例:
# 输入: sx = 1, sy = 1, tx = 3, ty = 5
# 输出: True
# 解释:
# 可以通过以下一系列转换从起点转换到终点：
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# 输入: sx = 1, sy = 1, tx = 2, ty = 2
# 输出: False
#
# 输入: sx = 1, sy = 1, tx = 1, ty = 1
# 输出: True
#
#
#
#  注意:
#
#
#  sx, sy, tx, ty 是范围在 [1, 10^9] 的整数。
#
#  Related Topics 数学
#  👍 53 👎 0

"""


import pytest


class Solution:

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        """
        回溯
        HARD
        https://leetcode-cn.com/problems/reaching-points/solution/dao-da-zhong-dian-by-leetcode/
        """
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy


class Solution1(object):
    """ 回溯 超时"""

    def reachingPoints(self, sx, sy, tx, ty):
        """
        通过求解父点完成 (x, y) -> (x-y, y) 或 (x, y-x) 的转换，具体使用哪一种转换取决于哪种结果没有负数。
        可以使用模运算加速求解父点的过程。

        """
        while tx >= sx and ty >= sy:
            if sx == tx and sy == ty:
                return True
            if tx > ty:
                tx -= ty
            else:
                ty -= tx
        return False


@pytest.mark.parametrize("kwargs,expected", [
    (dict(sx=1, sy=1, tx=3, ty=5), True),
    (dict(sx=1, sy=1, tx=2, ty=2), False),
    (dict(sx=1, sy=1, tx=1, ty=1), True),
])
def test_solutions(kwargs, expected):
    assert Solution().reachingPoints(**kwargs) == expected
    assert Solution1().reachingPoints(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
