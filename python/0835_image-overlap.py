#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。 
# 
#  我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。 
# 
#  （请注意，转换不包括向任何方向旋转。） 
# 
#  最大可能的重叠是什么？ 
# 
#  示例 1: 
# 
#  输入：A = [[1,1,0],
#           [0,1,0],
#          [0,1,0]]
#     B = [[0,0,0],
#          [0,1,1],
#          [0,0,1]]
# 输出：3
# 解释: 将 A 向右移动一个单位，然后向下移动一个单位。 
# 
#  注意: 
# 
#  
#  1 <= A.length = A[0].length = B.length = B[0].length <= 30 
#  0 <= A[i][j], B[i][j] <= 1 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        """
        GOOD
        只要是横纵坐标差相同的两对位置，一定是在同一次平移上
        """
        m, n = len(A), len(A[0])
        La, Lb = [], []
        counter = collections.Counter()
        for r in range(m):
            for c in range(n):
                if A[r][c] == 1:
                    La.append((r, c))
                if B[r][c] == 1:
                    Lb.append((r, c))
        for ax, ay in La:
            for bx, by in Lb:
                k = (ax - bx, ay - by)
                counter[k] += 1
        # print(counter)
        return max(counter.values() or [ 0])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A=[[1, 1, 0],
           [0, 1, 0],
           [0, 1, 0]],
        B=[[0, 0, 0],
           [0, 1, 1],
           [0, 0, 1]]
    ), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().largestOverlap(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
