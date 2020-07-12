#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 23:48:46
# @Last Modified : 2020-07-12 23:48:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。 
# 
#  示例1: 
# 
#  
#  输入：num = 2（或者0b10）
#  输出 1 (或者 0b01)
#  
# 
#  示例2: 
# 
#  
#  输入：num = 3
#  输出：3
#  
# 
#  提示: 
# 
#  
#  num的范围在[0, 2^30 - 1]之间，不会发生整数溢出。 
#  
#  Related Topics 位运算 
#  👍 20 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exchangeBits(self, num: int) -> int:
        """
        因此可以先操作奇数位，再操作偶数位。

        对于奇数位，使用 101010（即 0xAA）作为掩码，提取奇数位，并把它们右移一位；
        对于偶数位，使用 010101（即 0x55）作为掩码，提取偶数位，并把它们左移一位

        """
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)

# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(         num = 2                       ), 1],

    pytest.param(dict(        num = 3             ), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().exchangeBits(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

