#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 10:52:40
# @Last Modified : 2020-08-04 10:52:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个在 0 到 9 之间的整数 d，和两个正整数 low 和 high 分别作为上下界。返回 d 在 low 和 high 之间的整数中出现的次数，包括
# 边界 low 和 high。 
# 
#  
# 
#  示例 1： 
# 
#  输入：d = 1, low = 1, high = 13
# 输出：6
# 解释： 
# 数字 d=1 在 1,10,11,12,13 中出现 6 次。注意 d=1 在数字 11 中出现两次。
#  
# 
#  示例 2： 
# 
#  输入：d = 3, low = 100, high = 250
# 输出：35
# 解释：
# 数字 d=3 在 103,113,123,130,131,...,238,239,243 出现 35 次。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= d <= 9 
#  1 <= low <= high <= 2×10^8 
#  
#  Related Topics 数学 动态规划 
#  👍 12 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def countDigit(n):
            if n <= 0:
                return 0
            num, x, ans = n, 1, 0
            while num > 0:
                num, digit = divmod(num, 10)
                if d == 0:
                    ans -= x
                ans += num * x
                if digit == d:
                    ans += n % x + 1
                elif digit > d:
                    ans += x
                x *= 10
            return ans

        return countDigit(high) - countDigit(low - 1)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(d=1, low=1, high=13), 6],
    [dict(d=3, low=100, high=250), 35],
    [dict(d=0, low=100, high=250), 36],
    [dict(d=0, low=1, high=10), 1],
    [dict(d=0, low=1080, high=2160), 339],
])
def test_solutions(kw, expected):
    assert Solution().digitsCount(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
