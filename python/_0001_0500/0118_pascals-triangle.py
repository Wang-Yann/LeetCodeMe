#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 18:56:38
# @Last Modified : 2020-04-05 18:56:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  Related Topics 数组
#  👍 328 👎 0

"""
from typing import List

import pytest


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            cur_row = [1]
            prev = res[i - 1]
            for j in range(0, i - 1):
                cur_row.append(prev[j] + prev[j + 1])
            cur_row.append(1)
            res.append(cur_row)
        return res


class Solution1:

    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret


@pytest.mark.parametrize("args,expected", [
    (3, [[1], [1, 1], [1, 2, 1]]),
    (2, [[1], [1, 1]]),
    (7, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]])
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().generate(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
