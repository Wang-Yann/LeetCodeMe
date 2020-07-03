#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请你帮忙设计一个程序，用来找出第 n 个丑数。 
# 
#  丑数是可以被 a 或 b 或 c 整除的 正整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3, a = 2, b = 3, c = 5
# 输出：4
# 解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。 
# 
#  示例 2： 
# 
#  输入：n = 4, a = 2, b = 3, c = 4
# 输出：6
# 解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
#  
# 
#  示例 3： 
# 
#  输入：n = 5, a = 2, b = 11, c = 13
# 输出：10
# 解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
#  
# 
#  示例 4： 
# 
#  输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
# 输出：1999999984
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n, a, b, c <= 10^9 
#  1 <= a * b * c <= 10^18 
#  本题结果在 [1, 2 * 10^9] 的范围内 
#  
#  Related Topics 数学 二分查找

"""

import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
        GOOD
        For every integer A, F(A) = (total number of positive integers <= A which are divisible by a or b or c.).
        F(A) = A/a + A/b + A/c - A/lcm(a, c) - A/lcm(a, b) - A/lcm(a, c) + A/lcm(a, b, c)(lcm = least common multiple)
        Find the least integer A that satisfies the condition F(A) == n
        """

        def lcm(x, y):
            return x * y // math.gcd(x, y)

        def count_ugly(n, a, b, c, ab, bc, ca, abc):
            answer = n // a + n // b + n // c
            answer -= n // ab + n // bc + n // ca
            answer += n // abc
            return answer

        ab, bc, ca = lcm(a, b), lcm(b, c), lcm(c, a)
        abc = lcm(ab, c)
        low = 1
        high = 2 * 10 ** 9
        while low < high:
            mid = low + (high - low) //2
            if count_ugly(mid, a, b, c, ab, bc, ca, abc) < n:
                low = mid + 1
            else:
                high = mid
        return low


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=3, a=2, b=3, c=5), 4],
    [dict(n=4, a=2, b=3, c=4), 6],
    [dict(n=5, a=2, b=11, c=13), 10],
])
def test_solutions(kw, expected):
    assert Solution().nthUglyNumber(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
