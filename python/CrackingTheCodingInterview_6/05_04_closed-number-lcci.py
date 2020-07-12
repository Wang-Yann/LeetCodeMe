#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 23:43:25
# @Last Modified : 2020-07-12 23:43:25
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。 
# 
#  示例1: 
# 
#  
#  输入：num = 2（或者0b10）
#  输出：[4, 1] 或者（[0b100, 0b1]）
#  
# 
#  示例2: 
# 
#  
#  输入：num = 1
#  输出：[2, -1]
#  
# 
#  提示: 
# 
#  
#  num的范围在[1, 2147483647]之间； 
#  如果找不到前一个或者后一个满足条件的正数，那么输出 -1。 
#  
#  Related Topics 位运算 
#  👍 7 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findClosedNumbers(self, num: int) -> List[int]:
        left, right = num + 1, num - 1

        n = bin(num).count('1')

        while bin(left).count('1') != n:
            left += 1

        while right > 0 and bin(right).count('1') != n:
            right -= 1

        right = -1 if right == 0 else right

        return [left, right]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(num=2), [4, 1]],

    pytest.param(dict(num=1), [2, -1]),
])
def test_solutions(kwargs, expected):
    assert Solution().findClosedNumbers(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
