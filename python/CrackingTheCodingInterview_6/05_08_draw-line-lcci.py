#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 23:50:44
# @Last Modified : 2020-07-12 23:50:44
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 绘制直线。有个单色屏幕存储在一个一维数组中，使得32个连续像素可以存放在一个 int 里。屏幕宽度为w，且w可被32整除（即一个 int 不会分布在两行上）
# ，屏幕高度可由数组长度及屏幕宽度推算得出。请实现一个函数，绘制从点(x1, y)到点(x2, y)的水平线。 
# 
#  给出数组的长度 length，宽度 w（以比特为单位）、直线开始位置 x1（比特为单位）、直线结束位置 x2（比特为单位）、直线所在行数 y。返回绘制过后
# 的数组。 
# 
#  示例1: 
# 
#   输入：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
#  输出：[3]
#  说明：在第0行的第30位到第31为画一条直线，屏幕表示为[0b000000000000000000000000000000011]
#  
# 
#  示例2: 
# 
#   输入：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
#  输出：[-1, -1, -1]
#  
#  Related Topics 数组 
#  👍 3 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        """
        TODO TODO
        length代表int数量（9），w代表一行可以放几个int（3）,y代表在第几行。
        (1,1,1) y=0
        (1,1,1) y=1
        (1,1,1) y=2
        """
        anw = [0] * length
        wid = w // 32
        n1, m1 = divmod(x1, 32)
        n2, m2 = divmod(x2, 32)
        for i in range(wid * y + n1, wid * y + n2 + 1):
            anw[i] = -1
        if m1 != 0:
            anw[wid * y + n1] += 1 << (32 - m1)
        anw[wid * y + n2] -= (1 << (32 - m2 - 1)) - 1
        return anw


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(length=1, w=32, x1=30, x2=31, y=0), [3]],

    pytest.param(dict(length=3, w=96, x1=0, x2=95, y=0), [-1, -1, -1]),
])
def test_solutions(kwargs, expected):
    assert Solution().drawLine(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
