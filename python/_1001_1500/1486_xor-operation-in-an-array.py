#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 16:47:16
# @Last Modified : 2020-07-10 16:47:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个整数，n 和 start 。 
# 
#  数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。 
# 
#  请返回 nums 中所有元素按位异或（XOR）后得到的结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 5, start = 0
# 输出：8
# 解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
#      "^" 为按位异或 XOR 运算符。
#  
# 
#  示例 2： 
# 
#  输入：n = 4, start = 3
# 输出：8
# 解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8. 
# 
#  示例 3： 
# 
#  输入：n = 1, start = 7
# 输出：7
#  
# 
#  示例 4： 
# 
#  输入：n = 10, start = 5
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  0 <= start <= 1000 
#  n == nums.length 
#  
#  Related Topics 位运算 数组 
#  👍 3 👎 0

"""

import functools
import operator

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        """AC"""
        return functools.reduce(operator.xor, map(lambda x: 2 * x + start, range(n)))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(n=5, start=0), 8],
    [dict(n=4, start=3), 8],
    [dict(n=1, start=7), 7],
    [dict(n=10, start=5), 2],
])
def test_solutions(kw, expected):
    assert Solution().xorOperation(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
