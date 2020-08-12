#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 13:36:41
# @Last Modified : 2020-05-04 13:36:41
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#  示例 1:
#
#  输入: num1 = "2", num2 = "3"
# 输出: "6"
#
#  示例 2:
#
#  输入: num1 = "123", num2 = "456"
# 输出: "56088"
#
#  说明：
#
#
#  num1 和 num2 的长度小于110。
#  num1 和 num2 只包含数字 0-9。
#  num1 和 num2 均不以零开头，除非是数字 0 本身。
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#  Related Topics 数学 字符串
#  👍 387 👎 0

"""

import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        GOOD
        细心观察之后就发现，num1[i] 和 num2[j] 的乘积对应的就是 res[i+j] 和 res[i+j+1] 这两个位置
        """
        num1, num2 = num1[::-1], num2[::-1]
        N1, N2 = map(len, [num1, num2])
        res = [0] * (N1 + N2)
        for i in range(N1):
            for j in range(N2):
                res[i + j] += int(num1[i]) * int(num2[j])
                # print(res)
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        i = N1 + N2 - 1
        while i > 0 and res[i] == 0:
            i -= 1
        return "".join(map(str, res[i::-1]))


@pytest.mark.parametrize("kwargs,expected", [
    (dict(num1="2", num2="3"), "6"),
    pytest.param(dict(num1="123", num2="456"), "56088"),
])
def test_solutions(kwargs, expected):
    assert Solution().multiply(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
