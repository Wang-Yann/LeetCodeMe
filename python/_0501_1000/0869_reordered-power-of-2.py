#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:43:25
# @Last Modified : 2020-05-05 22:43:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
#
#  如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。
#
#
#
#
#
#
#  示例 1：
#
#  输入：1
# 输出：true
#
#
#  示例 2：
#
#  输入：10
# 输出：false
#
#
#  示例 3：
#
#  输入：16
# 输出：true
#
#
#  示例 4：
#
#  输入：24
# 输出：false
#
#
#  示例 5：
#
#  输入：46
# 输出：true
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#
#  Related Topics 数学
#  👍 32 👎 0

"""

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """ 既然 N 只能是 2 的幂，我们只需要检查 NN 跟这些幂是不是拥有一样数字构成"""
        count =collections.Counter(str(N))
        return any(count == collections.Counter(str(1<<b)) for b in range(31))


@pytest.mark.parametrize("args,expected", [
    (1, True),
    (10, False),
    (16, True),
    (24, False),
    (46, True),
    (281, True),
])
def test_solutions(args, expected):
    assert Solution().reorderedPowerOf2(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


