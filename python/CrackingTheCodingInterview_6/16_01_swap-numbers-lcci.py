#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:49:07
# @Last Modified : 2020-07-13 14:49:07
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。 
#  示例： 
#  输入: numbers = [1,2]
# 输出: [2,1]
#  
#  提示： 
#  
#  numbers.length == 2 
#  
#  Related Topics 位运算 数学 
#  👍 20 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        a, b = numbers
        tmp = a ^ b
        a ^= tmp
        b ^= tmp
        return [a, b]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(numbers=[1, 2]), [2, 1]],
])
def test_solutions(kw, expected):
    assert Solution().swapNumbers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
