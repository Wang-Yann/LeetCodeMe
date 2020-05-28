#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。 
# 
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下： 
# 
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#  
# 
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。 
# 
#  请你实现这个将字符串进行指定行数变换的函数： 
# 
#  string convert(string s, int numRows); 
# 
#  示例 1: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#  
# 
#  示例 2: 
# 
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# 
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G 
#  Related Topics 字符串

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        """
        https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
        """
        if numRows <= 1 or len(s) <= numRows:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for char in s:
            res[i] += char
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="LEETCODEISHIRING", numRows=3

          ), "LCIRETOESIIGEDHN"),
    pytest.param(dict(s="LEETCODEISHIRING", numRows=4), "LDREOEIIECIHNTSG"),
])
def test_solutions(kwargs, expected):
    assert Solution().convert(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
