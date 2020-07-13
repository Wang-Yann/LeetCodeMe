#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 20:15:29
# @Last Modified : 2020-07-13 20:15:29
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。 
# 
#  示例: 
# 
#  输入: a = 1, b = 1
# 输出: 2 
# 
#  
# 
#  提示： 
# 
#  
#  a, b 均可能是负数或 0 
#  结果不会溢出 32 位整数 
#  
#  Related Topics 位运算 
#  👍 16 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def add(self, a: int, b: int) -> int:
        MASK = 0xffffffff
        a &= MASK
        b &= MASK

        while b:
            sum_val = a ^ b
            carry = ((a & b) << 1) & MASK
            a = sum_val
            b = carry
        if a <= 0x7fffffff:
            return a
        # 如果是负数,转换成补码形式

        return ~(a ^ MASK)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(a=1, b=1), 2],
    [dict(a=-1, b=2), 1],
    [dict(a=121, b=2), 123],

])
def test_solutions(kwargs, expected):
    assert Solution().add(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
