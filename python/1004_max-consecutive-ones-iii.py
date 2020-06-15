#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。 
# 
#  返回仅包含 1 的最长（连续）子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释： 
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 20000 
#  0 <= K <= A.length 
#  A[i] 为 0 或 1 
#  
#  Related Topics 双指针 Sliding Window

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        ans = 0
        l = 0
        for r, v in enumerate(A):
            K -= int(v == 0)
            while K < 0:
                K += int(A[l] == 0)
                l += 1
            ans = max(ans, r - l + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(A=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], K=2), 2],
    [dict(A=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], K=3), 10],
])
def test_solutions(kw, expected):
    assert Solution().longestOnes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
