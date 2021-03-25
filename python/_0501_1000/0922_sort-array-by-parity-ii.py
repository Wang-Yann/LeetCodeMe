#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 15:20:17
# @Last Modified : 2020-05-03 15:20:17
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
#
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
#
#  你可以返回任何满足上述条件的数组作为答案。
#
#
#
#  示例：
#
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
#
#
#
#  提示：
#
#
#  2 <= A.length <= 20000
#  A.length % 2 == 0
#  0 <= A[i] <= 1000
#
#
#
#  Related Topics 排序 数组
#  👍 108 👎 0

"""
from typing import List

import pytest


class Solution:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i, j = 0, 1
        for v in A:
            if v % 2 == 1:
                res[j] = v
                j += 2
            else:
                res[i] = v
                i += 2
        return res


class Solution1:

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


@pytest.mark.parametrize("args,expected", [
    ([4, 2, 5, 7], [4, 5, 2, 7]),
])
def test_solutions(args, expected):
    res = Solution().sortArrayByParityII(args)
    for idx, v in enumerate(res):
        assert idx % 2 == v % 2
    res1 = Solution1().sortArrayByParityII(args)
    for idx, v in enumerate(res1):
        assert idx % 2 == v % 2


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
