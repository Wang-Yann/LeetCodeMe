#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。 
# 
#  找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i, j < n 。 
# 
#  你能在O(n)的时间解决这个问题吗？ 
# 
#  示例: 
# 
#  
# 输入: [3, 10, 5, 25, 2, 8]
# 
# 输出: 28
# 
# 解释: 最大的结果是 5 ^ 25 = 28.
#  
#  Related Topics 位运算 字典树

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/shu-zu-zhong-liang-ge-shu-de-zui-da-yi-huo-zhi-by-/
    """

    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L - 1, -1, -1):
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes
            # of length (L - i) in binary representation

            prefixes = {num >> i for num in nums}
            # print([bin(x) for x in  prefixes])
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= int(any(curr_xor ^ p in prefixes for p in prefixes))
        return max_xor


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([3, 10, 5, 25, 2, 8], 28),
])
def test_solutions(args, expected):
    assert Solution().findMaximumXOR(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
