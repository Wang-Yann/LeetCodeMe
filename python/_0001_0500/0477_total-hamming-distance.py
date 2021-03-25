#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。 
# 
#  计算一个数组中，任意两个数之间汉明距离的总和。 
# 
#  示例: 
# 
#  
# 输入: 4, 14, 2
# 
# 输出: 6
# 
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 
# 2 + 2 = 6.
#  
# 
#  注意: 
# 
#  
#  数组中元素的范围为从 0到 10^9。 
#  数组的长度不超过 10^4。 
#  
#  Related Topics 位运算

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/total-hamming-distance/solution/yi-ming-ju-chi-zong-he-by-leetcode/
        """

        res = 0
        for i in range(32):
            cnts = [0, 0]
            for num in nums:
                cnts[(num >> i) & 0b1] += 1
            res += cnts[0] * cnts[1]
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def totalHammingDistance(self, nums):
        """
        计算出每一位上的汉明距离的总和，再相加即可
        """
        # print(list(map('{:032b}'.format, nums)))
        bin_list = list(zip(*map('{:032b}'.format, nums)))
        return sum((b.count('0') * b.count('1')) for b in bin_list)


@pytest.mark.parametrize("args,expected", [
    ([4, 14, 2], 6)
])
def test_solutions(args, expected):
    assert Solution().totalHammingDistance(args) == expected
    assert Solution1().totalHammingDistance(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
