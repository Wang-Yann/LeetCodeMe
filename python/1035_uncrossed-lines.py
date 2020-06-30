#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。 
# 
#  现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。 
# 
#  以这种方法绘制线条，并返回我们可以绘制的最大连线数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：A = [1,4,2], B = [1,2,4]
# 输出：2
# 解释：
# 我们可以画出两条不交叉的线，如上图所示。
# 我们无法画出第三条不相交的直线，因为从 A[1]=4 到 B[2]=4 的直线将与从 A[2]=2 到 B[1]=2 的直线相交。 
# 
#  示例 2： 
# 
#  输入：A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# 输出：2 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 500 
#  1 <= B.length <= 500 
#  1 <= A[i], B[i] <= 2000 
#  
# 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """
        设 A[0] ~ A[x] 与 B[0] ~ B[y] 的最大连线数为 f(x, y)
        """
        NA = len(A)
        NB = len(B)

        dp = [[0 for _ in range(NB + 1)] for _ in range(NA + 1)]

        for i in range(NA):
            for j in range(NB):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[NA][NB]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A=[1, 4, 2], B=[1, 2, 4]
    ), 2),
    pytest.param(dict(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]), 3),
    pytest.param(dict(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().maxUncrossedLines(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
