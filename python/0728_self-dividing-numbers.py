#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:00:44
# @Last Modified : 2020-05-05 18:00:44
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 自除数 是指可以被它包含的每一位数除尽的数。
#
#  例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
#
#  还有，自除数不允许包含 0 。
#
#  给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。
#
#  示例 1：
#
#
# 输入：
# 上边界left = 1, 下边界right = 22
# 输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
#
#
#  注意：
#
#
#  每个输入参数的边界满足 1 <= left <= right <= 10000。
#
#  Related Topics 数学
#  👍 105 👎 0

"""


from typing import List

import pytest


class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num):
            cur = num
            while cur:
                cur, rest = divmod(cur, 10)
                if rest ==0 or num % rest != 0:
                    return False
            return True

        ans = []
        for i in range(left, right + 1):
            if is_self_dividing(i):
                ans.append(i)
        return ans


@pytest.mark.parametrize("left,right,expected", [
    (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
])
def test_solutions(left, right, expected):
    assert Solution().selfDividingNumbers(left, right) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
