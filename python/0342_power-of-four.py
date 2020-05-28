#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。 
# 
#  示例 1: 
# 
#  输入: 16
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: 5
# 输出: false 
# 
#  进阶： 
# 你能不使用循环或者递归来完成本题吗？ 
#  Related Topics 位运算

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        while num and not num & 0b11:
            num >>= 2
        return num == 1


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    (16, True),
    (4, True),
    (12, False),
    (-2147483648, False),
    pytest.param(5, False),
])
def test_solutions(args, expected):
    assert Solution().isPowerOfFour(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
