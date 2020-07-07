#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。 
# 
#  返回 至少 能删除数组中的一半整数的整数集合的最小大小。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,3,3,3,5,5,5,2,2,7]
# 输出：2
# 解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
# 大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
# 选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。
#  
# 
#  示例 2： 
# 
#  输入：arr = [7,7,7,7,7,7]
# 输出：1
# 解释：我们只能选择集合 {7}，结果数组为空。
#  
# 
#  示例 3： 
# 
#  输入：arr = [1,9]
# 输出：1
#  
# 
#  示例 4： 
# 
#  输入：arr = [1000,1000,3,7]
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：arr = [1,2,3,4,5,6,7,8,9,10]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  arr.length 为偶数 
#  1 <= arr[i] <= 10^5 
#  
#  Related Topics 贪心算法 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        N = len(arr)
        ans = 0
        cur = 0
        for k in sorted(counter.keys(), key=lambda x: -counter[x]):
            cur += counter[k]
            ans += 1
            if cur >= (N + 1) // 2:
                break
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]), 2],
    [dict(arr=[7, 7, 7, 7, 7, 7]), 1],
    [dict(arr=[1, 9]), 1],
    [dict(arr=[1000, 1000, 3, 7]), 1],
    [dict(arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5],
])
def test_solutions(kw, expected):
    assert Solution().minSetSize(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
