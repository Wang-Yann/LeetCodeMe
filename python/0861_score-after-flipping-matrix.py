#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。 
# 
#  移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。 
# 
#  在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。 
# 
#  返回尽可能高的分数。 
# 
#  
# 
#  
#  
# 
#  示例： 
# 
#  输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20 
#  1 <= A[0].length <= 20 
#  A[i][j] 是 0 或 1 
#  
#  Related Topics 贪心算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                A[i] = [bit ^ 1 for bit in A[i]]
        for col in range(n):
            sum_cnt = sum(A[row][col] for row in range(m))
            if 2 * sum_cnt < m:
                for row in range(m):
                    A[row][col] ^= 1
        return sum(int("".join(map(str, row)), 2) for row in A)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):

    def matrixScore(self, A):
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans


class Solution2(object):
    """
    Assume A is M * N.

        A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
        We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.
        A[i][j] is worth 1 << (N - 1 - j)
        For every col, I count the current number of 1s.
        After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
        if M - cur > cur, we can toggle this column to get more 1s.
        max(cur, M - cur) will be the maximum number of 1s that we can get.


    """

    def matrixScore(self, A):
        M, N = len(A), len(A[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = sum(A[i][j] == A[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res


@pytest.mark.parametrize("args,expected", [
    ([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]], 39),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1, Solution2])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().matrixScore(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
