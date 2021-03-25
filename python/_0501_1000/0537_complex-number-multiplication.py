#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:35:01
# @Last Modified : 2020-05-05 16:35:01
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定两个表示复数的字符串。
#
#  返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。
#
#  示例 1:
#
#
# 输入: "1+1i", "1+1i"
# 输出: "0+2i"
# 解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
#
#
#  示例 2:
#
#
# 输入: "1+-1i", "1+-1i"
# 输出: "0+-2i"
# 解释: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。
#
#
#  注意:
#
#
#  输入字符串不包含额外的空格。
#  输入字符串将以 a+bi 的形式给出，其中整数 a 和 b 的范围均在 [-100, 100] 之间。输出也应当符合这种形式。
#
#  Related Topics 数学 字符串
#  👍 34 👎 0


import pytest


class Solution:

    def complexNumberMultiply(self, a: str, b: str) -> str:
        ra, ia = map(int, a[:-1].split("+"))
        rb, ib = map(int, b[:-1].split("+"))
        return "%d+%di" % (ra * rb - ia * ib, ra * ib + ia * rb)


@pytest.mark.parametrize("a,b,expected", [
    ("1+1i", "1+1i", "0+2i"),
    pytest.param("1+-1i", "1+-1i", "0+-2i"),
])
def test_solutions(a, b, expected):
    assert Solution().complexNumberMultiply(a, b) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
