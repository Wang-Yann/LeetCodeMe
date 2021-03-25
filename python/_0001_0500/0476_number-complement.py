#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。 
# 
#  
# 
#  
#  
# 
#  示例 1: 
# 
#  输入: 5
# 输出: 2
# 解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
#  
# 
#  示例 2: 
# 
#  输入: 1
# 输出: 0
# 解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
#  
# 
#  
# 
#  注意: 
# 
#  
#  给定的整数保证在 32 位带符号整数的范围内。 
#  你可以假定二进制数不包含前导零位。 
#  本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同 
#  
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (5, 2),
    (1, 0),
])
def test_solutions(args, expected):
    assert Solution().findComplement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
