#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。 
# 
#  注意: 
# 
#  
#  十六进制中所有字母(a-f)都必须是小写。 
#  十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
#  给定的数确保在32位有符号整数范围内。 
#  不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。 
#  
# 
#  示例 1： 
# 
#  
# 输入:
# 26
# 
# 输出:
# "1a"
#  
# 
#  示例 2： 
# 
#  
# 输入:
# -1
# 
# 输出:
# "ffffffff"
#  
#  Related Topics 位运算

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = ""
        for i in range(8):
            n = num & 0b1111
            if n > 9:
                n = chr(ord('a') + (n-10))
            else:
                n = str(n)
            ans = n + ans
            num >>= 4
        return ans.lstrip('0')


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def toHex(self, num: int) -> str:
        num &= 0xffffffff
        return hex(num).replace("0x", "")


@pytest.mark.parametrize("args,expected", [
    (0, '0'),
    (26, '1a'),
    pytest.param(-1, "ffffffff"),
])
def test_solutions(args, expected):
    assert Solution().toHex(args) == expected
    assert Solution1().toHex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
