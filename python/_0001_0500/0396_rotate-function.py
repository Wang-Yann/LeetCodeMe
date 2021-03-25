#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 14:16:14
# @Last Modified : 2020-05-05 14:16:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个长度为 n 的整数数组 A 。
#
#  假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：
#
#  F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。
#
#  计算F(0), F(1), ..., F(n-1)中的最大值。
#
#  注意:
# 可以认为 n 的值小于 105。
#
#  示例:
#
#
# A = [4, 3, 2, 6]
#
# F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
#
# 所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
#
#  Related Topics 数学
#  👍 48 👎 0

"""

from typing import List

import pytest


class Solution:

    def maxRotateFunction(self, A: List[int]) -> int:
        """
        错位相减
        F(k+1) = F(k) + S - n * Bk[n-1]
        """
        sum_val = sum(A)
        fi = 0
        for i, v in enumerate(A):
            fi += i * v
        result = fi
        for i in range( len(A)-1,0,-1):
            fi += sum_val - len(A) * A[i]
            result = max(result, fi)
        return result


@pytest.mark.parametrize("args,expected", [
    ([4, 3, 2, 6], 26),
])
def test_solutions(args, expected):
    assert Solution().maxRotateFunction(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
