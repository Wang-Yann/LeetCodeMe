#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果序列 X_1, X_2, ..., X_n 满足下列条件，就说它是 斐波那契式 的： 
# 
#  
#  n >= 3 
#  对于所有 i + 2 <= n，都有 X_i + X_{i+1} = X_{i+2} 
#  
# 
#  给定一个严格递增的正整数数组形成序列，找到 A 中最长的斐波那契式的子序列的长度。如果一个不存在，返回 0 。 
# 
#  （回想一下，子序列是从原序列 A 中派生出来的，它从 A 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， [3, 5, 8] 是 [3
# , 4, 5, 6, 7, 8] 的一个子序列） 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入: [1,2,3,4,5,6,7,8]
# 输出: 5
# 解释:
# 最长的斐波那契式子序列为：[1,2,3,5,8] 。
#  
# 
#  示例 2： 
# 
#  输入: [1,3,7,11,12,14,18]
# 输出: 3
# 解释:
# 最长的斐波那契式子序列有：
# [1,11,12]，[3,11,14] 以及 [7,11,18] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= A.length <= 1000 
#  1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9 
#  （对于以 Java，C，C++，以及 C# 的提交，时间限制被减少了 50%） 
#  
#  Related Topics 数组 动态规划

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        """
        设 longest[i, j] 是结束在 [i, j] 的最长路径。那么 如果 (i, j) 和 (j, k) 是连通的， longest[j, k] = longest[i, j] + 1。
        由于 i 由 A.index(A[k] - A[j]) 唯一确定，所以这是有效的：我们在 i 潜在时检查每组 j < k，并相应地更新 longest[j, k]。
        """
        index = {x:i for i, x in enumerate(A)}
        longest = collections.defaultdict(lambda:2)
        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j])
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)
        return ans if ans >= 3 else 0


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        """
        暴力
        """
        S = set(A)
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                b, a = A[j], A[i] + A[j]
                length = 2
                while a in S:
                    b, a = a, a+b
                    length += 1
                ans = max(ans, length)
        return ans if ans >= 3 else 0


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 5),
    pytest.param([1, 3, 7, 11, 12, 14, 18], 3),
])
def test_solutions(args, expected):
    assert Solution().lenLongestFibSubseq(args) == expected
    assert Solution1().lenLongestFibSubseq(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
