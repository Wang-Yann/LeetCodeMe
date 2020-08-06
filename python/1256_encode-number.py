#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-06 18:32:20
# @Last Modified : 2020-08-06 18:32:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个非负整数 num ，返回它的「加密字符串」。 
# 
#  加密的过程是把一个整数用某个未知函数进行转化，你需要从下表推测出该转化函数： 
#
# n--f(n)
# 0--""
# 1--"0"
# 2--"1"
# 3--"00"
# 4--"01"
# 5--"10"
# 6--"11"
# 7--"000"
#
#  示例 1： 
# 
#  输入：num = 23
# 输出："1000"
#  
# 
#  示例 2： 
# 
#  输入：num = 107
# 输出："101100"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num <= 10^9 
#  
#  Related Topics 位运算 数学 
#  👍 12 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def encode(self, num: int) -> str:
        return bin(num + 1)[3:]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(num=23), "1000"],
    [dict(num=107), "101100"],
])
def test_solutions(kw, expected):
    assert Solution().encode(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
