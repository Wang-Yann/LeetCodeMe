#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 22:49:32
# @Last Modified : 2020-07-06 22:49:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你三个正整数 a、b 和 c。 
# 
#  你可以对 a 和 b 的二进制表示进行位翻转操作，返回能够使按位或运算 a OR b == c 成立的最小翻转次数。 
# 
#  「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：a = 2, b = 6, c = 5
# 输出：3
# 解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c 
# 
#  示例 2： 
# 
#  输入：a = 4, b = 2, c = 7
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：a = 1, b = 2, c = 3
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a <= 10^9 
#  1 <= b <= 10^9 
#  1 <= c <= 10^9 
#  
#  Related Topics 位运算 
#  👍 12 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minFlips(self, a: int, b: int, c: int) -> int:
        """
         a、b 和 c 二进制表示的第 i 位分别为 bit_a、bit_b 和 bit_c，根据 bit_c 的值，会有以下两种情况：
            若 bit_c 的值为 0，那么 bit_a 和 bit_b 必须都为 0，需要的翻转次数为 bit_a + bit_b；
            若 bit_c 的值为 1，那么 bit_a 和 bit_b 中至少有一个为 1，只有当它们都为 0 时，才需要 1 次翻转；

        """
        ans = 0
        for i in range(32):
            bit_a, bit_b, bit_c = (a >> i) & 0b1, (b >> i) & 0b1, (c >> i) & 0b1
            if bit_c == 0:
                ans += (bit_a + bit_b)
            else:
                if bit_a + bit_b == 0:
                    ans += 1
        return ans



# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        a=2, b=6, c=5
    ), 3),
    pytest.param(dict(a=4, b=2, c=7), 1),
    pytest.param(dict(a=1, b=2, c=3), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minFlips(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
