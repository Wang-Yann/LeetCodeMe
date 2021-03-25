#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 07:21:31
# @Last Modified : 2021-02-22 07:21:31
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数 n，你需要重复执行多次下述操作将其转换为 0 ： 
# 
#  
#  翻转 n 的二进制表示中最右侧位（第 0 位）。 
#  如果第 (i-1) 位为 1 且从第 (i-2) 位到第 0 位都为 0，则翻转 n 的二进制表示中的第 i 位。 
#  
# 
#  返回将 n 转换为 0 的最小操作次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出：2
# 解释：3 的二进制表示为 "11"
# "11" -> "01" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "01" -> "00" ，执行的是第 1 种操作。
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 6
# 输出：4
# 解释：6 的二进制表示为 "110".
# "110" -> "010" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
# "010" -> "011" ，执行的是第 1 种操作。
# "011" -> "001" ，执行的是第 2 种操作，因为第 0 位为 1 。
# "001" -> "000" ，执行的是第 1 种操作。
#  
# 
#  示例 4： 
# 
#  
# 输入：n = 9
# 输出：14
#  
# 
#  示例 5： 
# 
#  
# 输入：n = 333
# 输出：393
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 109 
#  
#  Related Topics 位运算 动态规划 
#  👍 35 👎 0

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    格雷码
    https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877798/JavaC%2B%2BPython-3-Solutions-with-Prove-O(1)-Space
    """

    @functools.lru_cache(None)
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        return n ^ self.minimumOneBitOperations(n >> 1)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=0), 0],
    [dict(n=3), 2],
    [dict(n=6), 4],
    [dict(n=9), 14],
    [dict(n=333), 393],
])
def test_solutions(kw, expected):
    assert Solution().minimumOneBitOperations(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
