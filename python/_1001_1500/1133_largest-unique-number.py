#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:12:44
# @Last Modified : 2020-08-04 17:12:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 A，请找出并返回在该数组中仅出现一次的最大整数。 
# 
#  如果不存在这个只出现一次的整数，则返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[5,7,3,9,4,9,8,3,1]
# 输出：8
# 解释： 
# 数组中最大的整数是 9，但它在数组中重复出现了。而第二大的整数是 8，它只出现了一次，所以答案是 8。
#  
# 
#  示例 2： 
# 
#  输入：[9,9,8,8]
# 输出：-1
# 解释： 
# 数组中不存在仅出现一次的整数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 2000 
#  0 <= A[i] <= 1000 
#  
#  Related Topics 数组 哈希表 
#  👍 8 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        for num in sorted(counter, reverse=True):
            if counter[num] == 1:
                return num
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
    ([9, 9, 8, 8], -1),
])
def test_solutions(args, expected):
    assert Solution().largestUniqueNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
