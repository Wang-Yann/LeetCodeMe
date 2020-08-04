#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:08:55
# @Last Modified : 2020-08-04 17:08:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设存在一个 k 位数 N，其每一位上的数字的 k 次幂的总和也是 N，那么这个数是阿姆斯特朗数。 
# 
#  给你一个正整数 N，让你来判定他是否是阿姆斯特朗数，是则返回 true，不是则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：153
# 输出：true
# 示例： 
# 153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3。
#  
# 
#  示例 2： 
# 
#  输入：123
# 输出：false
# 解释： 
# 123 是一个 3 位数，且 123 != 1^3 + 2^3 + 3^3 = 36。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 10^8 
#  
#  Related Topics 数学 
#  👍 4 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isArmstrong(self, N: int) -> bool:
        digits = [int(x) for x in str(N)]
        size = len(digits)
        return sum(x ** size for x in digits) == N


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (153, True),
    (123, False),
])
def test_solutions(args, expected):
    assert Solution().isArmstrong(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
