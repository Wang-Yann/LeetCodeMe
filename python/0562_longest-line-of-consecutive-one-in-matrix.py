#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 14:37:28
# @Last Modified : 2020-07-30 14:37:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个01矩阵 M，找到矩阵中最长的连续1线段。这条线段可以是水平的、垂直的、对角线的或者反对角线的。 
# 
#  示例: 
# 
#  输入:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# 输出: 3
#  
# 
#  提示: 给定矩阵中的元素数量不会超过 10,000。 
#  Related Topics 数组 
#  👍 20 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """GOOD"""
        if not M:
            return 0
        R = len(M)
        C = len(M[0])
        ans = 0
        dp = [[[0] * 4 for _ in range(C)] for __ in range(R)]
        for i in range(R):
            for j in range(C):
                if M[i][j] == 0:
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                if i - 1 >= 0:
                    dp[i][j][0] += dp[i - 1][j][0]
                if j - 1 >= 0:
                    dp[i][j][1] += dp[i][j - 1][1]
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j][2] += dp[i - 1][j - 1][2]
                if i - 1 >= 0 and j + 1 < C:
                    dp[i][j][3] += dp[i - 1][j + 1][3]
                ans = max(ans, max(dp[i][j]))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (
            [[0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 1]], 3
    )
])
def test_solutions(args, expected):
    assert Solution().longestLine(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
