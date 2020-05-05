#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:59:08
# @Last Modified : 2020-05-05 18:59:08
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
