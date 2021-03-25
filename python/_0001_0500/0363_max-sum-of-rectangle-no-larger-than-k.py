#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 15:25:50
# @Last Modified : 2020-04-27 15:25:50
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。
#
#  示例:
#
#  输入: matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出: 2
# 解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
#  说明：
#
#
#  矩阵内的矩形区域面积必须大于 0。
#  如果行数远大于列数，你将如何解答呢？
#
#  Related Topics 队列 二分查找 动态规划
#  👍 101 👎 0

"""

import bisect
from typing import List

import pytest


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        HARD TODO　TODO
        前缀和
            划分左右边界，并求出在此边界下，每行的总和
            通过二分法找不超过K的矩阵
        https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/gu-ding-zuo-you-bian-jie-qian-zhui-he-er-fen-by-po/
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        result = float("-inf")
        for left in range(col):
            # 以left为左边界，每行的总和
            row_sum = [0] * row  # 左边界改变才算区域的重新开始
            # 以 l、r 为左右界的，任意矩形的面积，即 rowSum 连续子数组 的 和
            for right in range(left, col):  # 枚举右边界
                for j in range(row):
                    row_sum[j] += matrix[j][right]  # 按每一行累计到 dp
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in row_sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr): result = max(cur - arr[loc], result)
                    # 把累加和加入
                    bisect.insort(arr, cur)
                # print("arr,cur,result,row_sum",arr,cur,result,row_sum)
        return result


class Solution1:
    """
     DP　会超时
    [Java,从暴力开始优化,配图配注释](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
    /solution/javacong-bao-li-kai-shi-you-hua-pei-tu-pei-zhu-shi/)
    """

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols, max_ans = len(matrix), len(matrix[0]), float("-inf")
        dp = [[[[0] * (cols + 1) for _ in range(rows + 1)] for _ in range(cols + 1)]
              for _ in range(rows + 1)]
        for i1 in range(1, rows + 1):
            for j1 in range(1, cols + 1):
                dp[i1][j1][i1][j1] = matrix[i1 - 1][j1 - 1]
                for i2 in range(i1, rows + 1):
                    for j2 in range(j1, cols + 1):
                        dp[i1][j1][i2][j2] = dp[i1][j1][i2 - 1][j2] + dp[i1][j1][i2][j2 - 1] \
                                             - dp[i1][j1][i2 - 1][j2 - 1] + matrix[i2 - 1][j2 - 1]
                        if max_ans < dp[i1][j1][i2][j2] <= k:
                            max_ans = dp[i1][j1][i2][j2]
        return max_ans


class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
       DP　会超时
        """
        rows, cols, max = len(matrix), len(matrix[0]), float("-inf")
        for i1 in range(1, rows + 1):
            for j1 in range(1, cols + 1):
                dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
                dp[i1][j1] = matrix[i1 - 1][j1 - 1]
                for i2 in range(i1, rows + 1):
                    for j2 in range(j1, cols + 1):
                        dp[i2][j2] = dp[i2 - 1][j2] + dp[i2][j2 - 1] \
                                     - dp[i2 - 1][j2 - 1] + matrix[i2 - 1][j2 - 1]
                        if max < dp[i2][j2] <= k:
                            max = dp[i2][j2]
        return max


@pytest.mark.parametrize("kw,expected", [
    [dict(matrix=[[1, 0, 1], [0, -2, 3]], k=2), 2],
])
def test_solutions(kw, expected):
    assert Solution().maxSumSubmatrix(**kw) == expected
    assert Solution1().maxSumSubmatrix(**kw) == expected
    assert Solution2().maxSumSubmatrix(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
