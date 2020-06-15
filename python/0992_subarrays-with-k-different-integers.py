#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。 
# 
#  （例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。） 
# 
#  返回 A 中好子数组的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,2,1,2,3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
#  
# 
#  示例 2： 
# 
#  输入：A = [1,2,1,3,4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  1 <= A[i] <= A.length 
#  1 <= K <= A.length 
#  
#  Related Topics 哈希表 双指针 Sliding Window

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMost(A, k):
            # print(A,k)
            counters = collections.Counter()
            l, r = 0, 0
            ans = 0
            while r <= len(A) - 1:
                counters[A[r]] += 1
                r += 1
                # print("Before : A {} | right {} ,left {} ".format(A, r, l))
                while len(counters) > k:
                    counters[A[l]] -= 1
                    if counters[A[l]] == 0:
                        counters.pop(A[l])
                    l += 1
                ans += r - l + 1
                # print("After  : A {} | right {} ,left {} ".format(A, r, l))
            return ans

        return atMost(A, K) - atMost(A, K - 1)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[1, 2, 1, 2, 3], K=2), 7],
    [dict(A=[1, 2, 1, 3, 4], K=3), 3],
])
def test_solutions(kw, expected):
    assert Solution().subarraysWithKDistinct(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
