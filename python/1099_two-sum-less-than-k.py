#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 15:46:08
# @Last Modified : 2020-08-04 15:46:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 A 和一个整数 K，请在该数组中找出两个元素，使它们的和小于 K 但尽可能地接近 K，返回这两个元素的和。 
# 
#  如不存在这样的两个元素，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [34,23,1,24,75,33,54,8], K = 60
# 输出：58
# 解释：
# 34 和 24 相加得到 58，58 小于 60，满足题意。
#  
# 
#  示例 2： 
# 
#  输入：A = [10,20,30], K = 15
# 输出：-1
# 解释：
# 我们无法找到和小于 15 的两个元素。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i] <= 1000 
#  1 <= K <= 2000 
#  
#  Related Topics 数组 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        """还没领会?"""
        A.sort()
        l, r = 0, len(A) - 1
        res = -1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l] + A[r])
                l += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[34, 23, 1, 24, 75, 33, 54, 8], K=60), 58],
    [dict(A=[10, 20, 30], K=15), -1],
])
def test_solutions(kw, expected):
    assert Solution().twoSumLessThanK(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
