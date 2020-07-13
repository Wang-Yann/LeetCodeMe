#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 16:42:54
# @Last Modified : 2020-07-13 16:42:54
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数，打印该整数的英文描述。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: "One Hundred Twenty Three"
#  
# 
#  示例 2: 
# 
#  输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five" 
# 
#  示例 3: 
# 
#  输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven" 
# 
#  示例 4: 
# 
#  输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thou
# sand Eight Hundred Ninety One" 
#  Related Topics 数学 字符串 
#  👍 7 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numberToWords(self, num: int) -> str:
        """
        TODO
        """

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return LESS_THAN_20[num] + " "
            elif num < 100:
                return TENS[num // 10] + " " + helper(num % 10)
            else:
                return LESS_THAN_20[num // 100] + " Hundred " + helper(num % 100)

        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(THOUSANDS)):
            if num % 1000:
                res = helper(num % 1000) + THOUSANDS[i] + " " + res
            num //= 1000
        return res.strip()


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (123, "One Hundred Twenty Three"),
    (12345, "Twelve Thousand Three Hundred Forty Five"),
    (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
    (1234567891,
     "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"),
])
def test_solutions(args, expected):
    assert Solution().numberToWords(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
