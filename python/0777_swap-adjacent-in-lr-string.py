#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或
# 者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回T
# rue。 
# 
#  
# 
#  示例 : 
# 
#  输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= len(start) = len(end) <= 10000。 
#  start和end中的字符串仅限于'L', 'R'和'X'。 
#  
#  Related Topics 脑筋急转弯

"""

import operator

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        把'X'看成空格
        第 n 个 'L' 不可能移动到初始位置的右边，第 n 个 'R' 不可能移动到初始位置的左边，我们把这个特性称为 “可到达性
        转换不变性 和 可到达性，在算法中可以分别检查这两个性质是否满足
        """
        if start.replace('X', '') != end.replace('X', ''):
            return False

        for (symbol, op) in (('L', operator.lt), ('R', operator.gt)):
            B = (i for i, c in enumerate(end) if c == symbol)
            for start_i, char in enumerate(start):
                if char == symbol and op(start_i, next(B)):
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(start="RXXLRXRXL", end="XRLXXRRLX"), True],
])
def test_solutions(kw, expected):
    assert Solution().canTransform(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
