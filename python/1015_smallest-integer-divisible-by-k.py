#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。 
# 
#  返回 N 的长度。如果不存在这样的 N，就返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：1
# 输出：1
# 解释：最小的答案是 N = 1，其长度为 1。 
# 
#  示例 2： 
# 
#  输入：2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 N 。 
# 
#  示例 3： 
# 
#  输入：3
# 输出：3
# 解释：最小的答案是 N = 111，其长度为 3。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= K <= 10^5 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        res = 0
        for N in range(1, K + 1):
            res = (res * 10 + 1) % K
            if not res:
                return N
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, 1),
    (2, -1),
    (3, 3),
    (17, 16),
    (13, 6),
])
def test_solutions(args, expected):
    assert Solution().smallestRepunitDivByK(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
