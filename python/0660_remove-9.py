#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 21:30:28
# @Last Modified : 2020-07-26 21:30:28
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 从 1 开始，移除所有包含数字 9 的所有整数，例如 9，19，29，…… 
# 
#  这样就获得了一个新的整数数列：1，2，3，4，5，6，7，8，10，11，…… 
# 
#  给定正整数 n，请你返回新数列中第 n 个数字是多少。1 是新数列中的第一个数字。 
# 
#  
# 
#  样例 1: 
# 
#  输入: 9
# 输出: 10
#  
# 
#  
# 
#  注释 ：n 不会超过 9 x 10^8。 
#  Related Topics 数学 
#  👍 6 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def newInteger(self, n: int) -> int:
        """这些数字看起来就是 9 进制数字！ """
        ans = ""
        while n:
            ans = "%d%s" % (n % 9, ans)
            n //= 9
        return int(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (9, 10),
    (109, 131),
    (899, 1208),
])
def test_solutions(args, expected):
    assert Solution().newInteger(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
