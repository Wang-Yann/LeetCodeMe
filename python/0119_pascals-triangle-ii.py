#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 3
# 输出: [1,3,3,1]
#
#
#  进阶：
#
#  你可以优化你的算法到 O(k) 空间复杂度吗？
#  Related Topics 数组
#  👍 163 👎 0
from typing import List

import pytest


class Solution:

    def getCn(self, n, i):
        if i == 0 or n == i:
            return 1
        res = 1
        for v in range(n, n - i, -1):
            res *= v
        for vv in range(1, i + 1):
            res //= vv
        return res

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        n = rowIndex
        res = [self.getCn(n, i) for i in range(rowIndex + 1)]
        return res


@pytest.mark.parametrize("args,expected", [
    (3, [1, 3, 3, 1]),
    (2, [1, 2, 1]),
    (5, [1, 5, 10, 10, 5, 1]),
])
def test_solutions(args, expected):
    assert Solution().getRow(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
