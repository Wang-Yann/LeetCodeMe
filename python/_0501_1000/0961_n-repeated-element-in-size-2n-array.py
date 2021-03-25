#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。 
# 
#  返回重复了 N 次的那个元素。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,3]
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：[2,1,2,5,3,2]
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：[5,1,5,2,5,3,5,4]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  4 <= A.length <= 10000 
#  0 <= A[i] < 10000 
#  A.length 为偶数 
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N = len(A)
        counter = collections.Counter(A)
        for k, v in counter.items():
            if v == N // 2:
                return k


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 3], 3),
    ([2, 1, 2, 5, 3, 2], 2),
    ([5, 1, 5, 2, 5, 3, 5, 4], 5),
])
def test_solutions(args, expected):
    assert Solution().repeatedNTimes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
