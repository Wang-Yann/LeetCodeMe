#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 不使用运算符 + 和 - ，计算两整数 a 、b 之和。 
# 
#  示例 1: 
#
#  输入: a = 1, b = 2
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: a = -2, b = 3
# 输出: 1 
#  Related Topics 位运算

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getSum(self, a: int, b: int) -> int:
        """
        在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，这就需要我们手动对 Python 中的整数进行处理，
        手动模拟 32 位 INT 整型。
        具体做法是将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0

        """
        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX_INT else ~(a ^ MASK)

    def minus(self, a, b):
        b = self.getSum(~b, 1)
        return self.getSum(a, b)

    def divide(self, a, b):
        isNeg = (a > 0) ^ (b > 0)
        x = a if a > 0 else self.getSum(~a, 1)
        y = b if b > 0 else self.getSum(~b, 1)
        ans = 0
        for i in range(31, -1, -1):
            if (x >> i) >= y:
                x = self.minus(x, y << i)
                ans = self.getSum(ans, 1 << i)
        return self.getSum(~ans, 1) if isNeg else ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def getSum(self, a: int, b: int) -> int:
        """
        在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，这就需要我们手动对 Python 中的整数进行处理，
        手动模拟 32 位 INT 整型。
        具体做法是将整数对 0x100000000 取模，保证该数从 32 位开始到最高位都是 0

        return # 其实可以简化为~(a ^ mask) 为什么要对负数做这样的处理呢？ 因为在python中int不是32位的，输出是64位，所以一个负数比如-2, 64位表示就是0x00000000FFFFFFFE, 用python求取这个16进制的值int('0x00000000FFFFFFFE', 16), 得到的数字是4294967294 不是我们想要的-2，所以： a^mask是先对a的前32位取反，对应-2，就得到0x0000000000000002 再用～操作符对所以位置取反，对应-2，得到0xFFFFFFFFFFFFFFFE

        """
        MASK = 0x100000000
        MAX_INT = 0x7fffffff
        MIN_INT = MAX_INT + 1
        while b:
            carry = (a & b) << 1  # // 计算进位
            a = (a ^ b) % MASK  # // 计算低位
            b = carry % MASK

        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(a=1, b=2), 3),
    pytest.param(dict(a=-2, b=3), 1),
])
def test_solutions(kwargs, expected):
    assert Solution1().getSum(**kwargs) == expected


def test_solutions_full():
    sol = Solution()
    assert sol.getSum(-11, 88) == 77
    assert sol.minus(-11, 88) == -99
    assert sol.divide(-100, -10) == 10
    assert sol.divide(100, -10) == -10


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
