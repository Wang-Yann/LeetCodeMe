#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-17 11:51:29
# @Last Modified : 2020-07-17 11:51:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0


# 给你一个只包含 0 和 1 的 rows * columns 矩阵 mat ，请你返回有多少个 子矩形 的元素全部都是 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：mat = [[1,0,1],
#            [1,1,0],
#            [1,1,0]]
# 输出：13
# 解释：
# 有 6个 1x1 的矩形。
# 有 2 个 1x2 的矩形。
# 有 3 个 2x1 的矩形。
# 有 1 个 2x2 的矩形。
# 有 1 个 3x1 的矩形。
# 矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13。
#  
# 
#  示例 2： 
# 
#  
# 输入：mat = [[0,1,1,0],
#            [0,1,1,1],
#            [1,1,1,0]]
# 输出：24
# 解释：
# 有 8 个 1x1 的子矩形。
# 有 5 个 1x2 的子矩形。
# 有 2 个 1x3 的子矩形。
# 有 4 个 2x1 的子矩形。
# 有 2 个 2x2 的子矩形。
# 有 2 个 3x1 的子矩形。
# 有 1 个 3x2 的子矩形。
# 矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。
#  
# 
#  示例 3： 
# 
#  
# 输入：mat = [[1,1,1,1,1,1]]
# 输出：21
#  
# 
#  示例 4： 
# 
#  
# 输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rows <= 150 
#  1 <= columns <= 150 
#  0 <= mat[i][j] <= 1 
#  
#  Related Topics 动态规划 
#  👍 38 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        GOOD
        ByteDance
        矩阵里每个点(i.j)统计他这行左边到他这个位置最多有几个连续的1，存为left[i][j]。然后对于每个点(i.j)，
        我们固定子矩形的右下角为(i.j)，利用left从该行i向上寻找子矩阵左上角为第k行的矩阵个数。每次将子矩阵个数加到答案中

        以节点(i , j ) 作为矩形右下角的所有矩形总个数 =
            以节点(i , j ) 作为矩形右上角 以节点(i , j ) 作为矩形右下角 的矩阵个数 +
            以节点(i-1 , j ) 作为矩形右上角 以节点(i , j ) 作为矩形右下角 的矩阵个数 + ...
            以节点(i-2 , j ) 作为矩形右上角 以节点(i , j ) 作为矩形右下角 的矩阵个数 + ...
            以节点(k , j ) 作为矩形右上角 以节点(i , j ) 作为矩形右下角 的矩阵个数 + ...
            以节点(0 , j ) 作为矩形右上角 以节点(i , j ) 作为矩形右下角 的矩阵个数；

        """
        M, N = len(mat), len(mat[0])
        left = [[0] * N for _ in range(M)]
        for i in range(M):
            now = 0
            for j in range(N):
                if mat[i][j] == 1:
                    now += 1
                else:
                    now = 0
                left[i][j] = now
        # print(left)
        ans = 0
        for i in range(M):
            for j in range(N):
                # // i, j is the top most left point of the rectangle which is fixed
                minx = 0x7fffffff
                for k in range(i, -1, -1):
                    minx = min(left[k][j], minx)
                    # print(i,j,k,minx)
                    ans += minx
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):
    def numSubmat(self, mat):
        """https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/720265/Java-Detailed-Explanation-From-O(MNM)-to-O(MN)-by-using-Stack"""

        def count(heights):
            dp, stk = [0] * len(heights), []
            for i in range(len(heights)):
                while stk and heights[stk[-1]] >= heights[i]:
                    stk.pop()
                dp[i] = dp[stk[-1]] + heights[i] * (i - stk[-1]) if stk else heights[i] * (i - 0 + 1)
                stk.append(i)
            return sum(dp)

        ans = 0
        A = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                A[j] = A[j] + 1 if mat[i][j] == 1 else 0
            ans += count(A)
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(
        mat=[[1, 0, 1],
             [1, 1, 0],
             [1, 1, 0]]
    ), 13],
    [dict(
        mat=[[0, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 1, 1, 0]]
    ), 24],
    [dict(
        mat=[[1, 1, 1, 1, 1, 1]]
    ), 21],
    [dict(
        mat=[[1, 0, 1],
             [0, 1, 0],
             [1, 0, 1]]
    ), 5],
])
def test_solutions(kw, expected):
    assert Solution().numSubmat(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
