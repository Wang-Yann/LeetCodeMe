#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 16:39:55
# @Last Modified : 2020-07-13 16:39:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。 
#  示例： 
#  输入： a = 1, b = 2
# 输出： 2
#  
#  Related Topics 位运算 数学 
#  👍 44 👎 0

"""

import math

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximum(self, a: int, b: int) -> int:
        """Haha"""
        return int((math.fabs(a - b) + a + b) / 2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(a=1, b=2), 2],
])
def test_solutions(kw, expected):
    assert Solution().maximum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
