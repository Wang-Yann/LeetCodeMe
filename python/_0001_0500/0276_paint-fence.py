#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 23:19:31
# @Last Modified : 2020-07-22 23:19:31
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，每个栅栏柱可以用其中一种颜色进行上色。 
# 
#  你需要给所有栅栏柱上色，并且保证其中相邻的栅栏柱 最多连续两个 颜色相同。然后，返回所有有效涂色的方案数。 
# 
#  注意: 
# n 和 k 均为非负的整数。 
# 
#  示例: 
# 
#  输入: n = 3，k = 2
# 输出: 6
# 解析: 用 c1 表示颜色 1，c2 表示颜色 2，所有可能的涂色方案有:
# 
#             柱 1    柱 2   柱 3     
#  -----      -----  -----  -----       
#    1         c1     c1     c2 
#    2         c1     c2     c1 
#    3         c1     c2     c2 
#    4         c2     c1     c1  
#    5         c2     c1     c2
#    6         c2     c2     c1
#  
#  Related Topics 动态规划 
#  👍 47 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numWays(self, n: int, k: int) -> int:
        """
        dp[i][0]: 涂第i个栅栏，且和前一个用的颜色不一样
        dp[i][1]: 涂第i个栅栏，且和前一个用的颜色一样
        """
        if not n or not k:
            return 0

        dp = [[0, 0] for _ in range(n)]
        dp[0] = [k, 0]

        for i in range(1, n):
            dp[i][0] = (k - 1) * sum(dp[i - 1])
            dp[i][1] = dp[i - 1][0]

        return sum(dp[n - 1])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=3, k=2), 6],

])
def test_solutions(kwargs, expected):
    assert Solution().numWays(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
