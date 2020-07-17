#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20


"""
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
#  你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#  示例 1:
#
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
#  示例 2:
#
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#  Related Topics 数组
#  👍 500 👎 0

"""

from typing import List


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        v_sum = digits[i]+1
        carry = v_sum // 10
        digits[i] = v_sum % 10
        i -= 1
        while i >= 0:
            v_sum = digits[i] + carry
            digits[i] = v_sum % 10
            carry = v_sum // 10
            if not carry:
                break
            i-=1
        if carry:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))
    print(sol.plusOne([9, 9]))
    print(sol.plusOne([ 1]))
