#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你需要找到由两个 n 位数的乘积组成的最大回文数。 
# 
#  由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。 
# 
#  示例: 
# 
#  输入: 2 
# 
#  输出: 987 
# 
#  解释: 99 x 91 = 9009, 9009 % 1337 = 987 
# 
#  说明: 
# 
#  n 的取值范围为 [1,8]。 
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper, lower = 10 ** n - 1, 10 ** (n - 1)
        for v in range(upper, lower - 1, -1):
            candidate = int(str(v) + str(v)[::-1])
            j = upper
            while j * j >= candidate:
                if candidate % j == 0:
                    return candidate % 1337
                j -= 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (2, 987)
])
def test_solutions(args, expected):
    assert Solution().largestPalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
