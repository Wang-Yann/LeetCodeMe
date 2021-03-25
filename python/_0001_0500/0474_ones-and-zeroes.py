#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在计算机界中，我们总是追求用有限的资源获取最大的收益。 
# 
#  现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。 
# 
#  你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。 
# 
#  注意: 
# 
#  
#  给定 0 和 1 的数量都不会超过 100。 
#  给定字符串数组的长度不会超过 600。 
#  
# 
#  示例 1: 
# 
#  
# 输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# 输出: 4
# 
# 解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
#  
# 
#  示例 2: 
# 
#  
# 输入: Array = {"10", "0", "1"}, m = 1, n = 1
# 输出: 2
# 
# 解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """背包"""
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zero_cnt, one_cnt = 0, 0
            for char in s:
                if char == "0":
                    zero_cnt += 1
                elif char == "1":
                    one_cnt += 1
            for i in range(m, zero_cnt - 1, -1):
                for j in range(n, one_cnt - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_cnt][j - one_cnt] + 1)
        return dp[m][n]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(strs={"10", "0001", "111001", "1", "0"}, m=5, n=3), 4],
    [dict(strs={"10", "0", "1"}, m=1, n=1), 2],
])
def test_solutions(kw, expected):
    assert Solution().findMaxForm(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
