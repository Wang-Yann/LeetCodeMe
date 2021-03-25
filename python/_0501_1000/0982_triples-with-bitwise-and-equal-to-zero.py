#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 A，找出索引为 (i, j, k) 的三元组，使得： 
# 
#  
#  0 <= i < A.length 
#  0 <= j < A.length 
#  0 <= k < A.length 
#  A[i] & A[j] & A[k] == 0，其中 & 表示按位与（AND）操作符。 
#  
# 
#  
# 
#  示例： 
# 
#  输入：[2,1,3]
# 输出：12
# 解释：我们可以选出如下 i, j, k 三元组：
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 1000 
#  0 <= A[i] < 2^16 
#  
#  Related Topics 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        """暴力"""
        counter = collections.Counter()
        N = len(A)
        for i in range(N):
            for j in range(N):
                counter[A[i] & A[j]] += 1
        ans = 0
        for num in A:
            for v in counter:
                if num & v == 0:
                    ans += counter[v]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([2, 1, 3], 12)
])
def test_solutions(args, expected):
    assert Solution().countTriplets(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
