#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:40:58
# @Last Modified : 2020-05-05 17:40:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。
#
#  示例 1 :
#
#
# 输入: 2736
# 输出: 7236
# 解释: 交换数字2和数字7。
#
#
#  示例 2 :
#
#
# 输入: 9973
# 输出: 9973
# 解释: 不需要交换。
#
#
#  注意:
#
#
#  给定数字的范围是 [0, 108]
#
#  Related Topics 数组 数学
#  👍 87 👎 0

import pytest


class Solution:

    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        left, right = 0, 0
        max_idx = len(digits) - 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[i] < digits[max_idx]:
                left, right = i, max_idx
        # print(left,right)
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))


@pytest.mark.parametrize("args,expected", [
    (2736, 7236),
    pytest.param(9973, 9973),
])
def test_solutions(args, expected):
    assert Solution().maximumSwap(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
