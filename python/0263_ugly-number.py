#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 22:01:23
# @Last Modified : 2020-04-27 22:01:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 编写一个程序判断给定的数是否为丑数。
#
#  丑数就是只包含质因数 2, 3, 5 的正整数。
#
#  示例 1:
#
#  输入: 6
# 输出: true
# 解释: 6 = 2 × 3
#
#  示例 2:
#
#  输入: 8
# 输出: true
# 解释: 8 = 2 × 2 × 2
#
#
#  示例 3:
#
#  输入: 14
# 输出: false
# 解释: 14 不是丑数，因为它包含了另外一个质因数 7。
#
#  说明：
#
#
#  1 是丑数。
#  输入不会超过 32 位有符号整数的范围: [−231, 231 − 1]。
#
#  Related Topics 数学
#  👍 136 👎 0

"""

class Solution:

    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i

        return abs(num) == 1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        -10,0,1,6,8,14,
        -2147483648
    ]
    res = [sol.isUgly(args) for args in samples]
    print(res)
