#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 15:42:33
# @Last Modified : 2020-07-27 15:42:33
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个 稀疏矩阵 A 和 B，请你返回 AB 的结果。你可以默认 A 的列数等于 B 的行数。 
# 
#  请仔细阅读下面的示例。 
# 
#  
# 
#  示例： 
# 
#  输入：
# 
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
# 
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
# 
# 输出：
# 
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
#  
#  Related Topics 哈希表 
#  👍 19 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n, l = len(A), len(A[0]), len(B[0])
        C = [[0] * l for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(l):
                        C[i][k] += A[i][j] * B[j][k]
        return C


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        A=[
            [1, 0, 0],
            [-1, 0, 3]
        ],

        B=[
            [7, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]

    ), [[7, 0, 0], [-7, 0, 3]]],
])
def test_solutions(kw, expected):
    assert Solution().multiply(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
