#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 11:40:39
# @Last Modified : 2020-08-07 11:40:39
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有一个十进制数字，请按照此规则将它变成「十六进制魔术数字」：首先将它变成字母大写的十六进制字符串，然后将所有的数字 0 变成字母 O ，将数字 1 变成字
# 母 I 。 
# 
#  如果一个数字在转换后只包含 {"A", "B", "C", "D", "E", "F", "I", "O"} ，那么我们就认为这个转换是有效的。 
# 
#  给你一个字符串 num ，它表示一个十进制数 N，如果它的十六进制魔术数字转换是有效的，请返回转换后的结果，否则返回 "ERROR" 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：num = "257"
# 输出："IOI"
# 解释：257 的十六进制表示是 101 。
#  
# 
#  示例 2： 
# 
#  输入：num = "3"
# 输出："ERROR"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10^12 
#  给定字符串不会有前导 0 。 
#  结果中的所有字母都应该是大写字母。 
#  
#  Related Topics 数学 字符串 
#  👍 4 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def toHexspeak(self, num: str) -> str:
        num = hex(int(num))[2:]
        S = ""
        for char in num:
            if char == "1":
                S += "I"
            elif char == "0":
                S += "O"
            else:
                S += char.upper()
        if not set(S) - {"A", "B", "C", "D", "E", "F", "I", "O"}:
            return S
        return "ERROR"


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(num="257"), "IOI"],
    [dict(num="3"), "ERROR"],
])
def test_solutions(kw, expected):
    assert Solution().toHexspeak(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
