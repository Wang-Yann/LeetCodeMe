#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:51:45
# @Last Modified : 2020-05-04 20:51:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
#
#  示例:
#
#  输入: 13
# 输出: 6
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
#  Related Topics 数学
#  👍 141 👎 0

"""

import pytest


class Solution:

    def countDigitOne(self, n: int) -> int:
        """https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/

        将 i 从 1 遍历到 n，每次遍历 i 扩大 10 倍：
        (n/(i*10))*i 表示 i*10 位上1的个数

        min(max((n mod (i*10)) -i +1,0),i) 表示需要额外数的（i×10)位上 1 的个数

        """
        ans = 0
        pivot = 1
        while pivot <= n:
            divider = pivot * 10
            ans += (n // divider) * pivot + min(max(n % divider - pivot + 1, 0), pivot)
            pivot = divider
        return ans


class Solution1:
    def countDigitOne(self, n: int) -> int:
        """
        https://leetcode.com/problems/number-of-digit-one/discuss/64382/JavaPython-one-pass-solution-easy-to-understand
        if n = xyzdabc
        and we are considering the occurrence of one on thousand, it should be:

        (1) xyz * 1000                     if d == 0
        (2) xyz * 1000 + abc + 1           if d == 1
        (3) xyz * 1000 + 1000              if d > 1
        
        """
        if n <= 0:
            return 0
        num, x, ans = n, 1, 0
        while num > 0:
            digit = num % 10
            num //= 10
            ans += num * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans


class Solution2:
    def countDigitOne(self, n: int) -> int:
        """
        https://leetcode.com/problems/number-of-digit-one/discuss/64382/JavaPython-one-pass-solution-easy-to-understand
        """
        if n < 1:
            return 0
        if 1 <= n <= 9:
            return 1
        x, y = n, 1
        while x >= 10:
            x //= 10
            y *= 10
        # print(x,y,n)
        if x == 1:
            return n - y + 1 + self.countDigitOne(y - 1) + self.countDigitOne(n % y)
        else:
            return y + x * self.countDigitOne(y - 1) + self.countDigitOne(n % y)




@pytest.mark.parametrize("args,expected", [
    (23416, 20089),
    (123416, 93506),
    (13, 6),
    pytest.param(8, 1),
])
def test_solutions(args, expected):
    assert Solution().countDigitOne(args) == expected
    assert Solution1().countDigitOne(args) == expected
    assert Solution2().countDigitOne(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
