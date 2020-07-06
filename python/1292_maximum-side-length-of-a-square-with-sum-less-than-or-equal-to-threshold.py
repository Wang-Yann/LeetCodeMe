#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。 
# 
#  请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于 4 的正方形的最大边长为 2，如图所示。
#  
# 
#  示例 2： 
# 
#  输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], thres
# hold = 1
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold 
# = 40184
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m, n <= 300 
#  m == mat.length 
#  n == mat[i].length 
#  0 <= mat[i][j] <= 10000 
#  0 <= threshold <= 10^5 
#  
#  Related Topics 数组 二分查找

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """二维前缀和"""
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        def check(mid):
            for i in range(mid, m + 1):
                for j in range(mid, n + 1):
                    if dp[i][j] + dp[i - mid][j - mid] - dp[i - mid][j] - dp[i][j - mid] <= threshold:
                        return True
            return False

        l, r = 0, min(m+1, n + 1)
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                l += 1
            else:
                r = mid - 1
        return r


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], threshold=4), 2],
    [dict(mat=[[2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2]], threshold=1), 0],
    [dict(mat=[[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], threshold=6), 3],
    [dict(mat=[[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], threshold=40184), 2],
])
def test_solutions(kw, expected):
    assert Solution().maxSideLength(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
