#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个方形整数数组 A，我们想要得到通过 A 的下降路径的最小和。 
# 
#  下降路径可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列。 
# 
#  
# 
#  示例： 
# 
#  输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：12
# 解释：
# 可能的下降路径有：
#  
# 
#  
#  [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9] 
#  [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9] 
#  [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9] 
#  
# 
#  和最小的下降路径是 [1,4,7]，所以答案是 12。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length == A[0].length <= 100 
#  -100 <= A[i][j] <= 100 
#  
#  Related Topics 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        """
        从倒数第二行开始，从下往上进行动态规划，状态转移方程为：

        A[r][c] = A[r][c] + min{A[r + 1][c - 1], A[r + 1][c], A[r + 1][c + 1]}
        https://www.jiuzhang.com/solution/minimum-falling-path-sum
        """
        R, C = len(A), len(A[0])
        for i in range(1, R):
            for j in range(C):
                top_left = A[i - 1][max(j - 1, 0)]
                top_right = A[i - 1][min(j + 1, R - 1)]
                A[i][j] += min(top_left, top_right, A[i - 1][j])
        # print(A)
        return min(A[-1])


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
            , 12),
])
def test_solutions(args, expected):
    assert Solution().minFallingPathSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
