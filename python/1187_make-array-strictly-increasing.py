#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。 
# 
#  每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j 
# < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。 
# 
#  如果无法让 arr1 严格递增，请返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
#  
# 
#  示例 2： 
# 
#  输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
#  
# 
#  示例 3： 
# 
#  输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length <= 2000 
#  0 <= arr1[i], arr2[i] <= 10^9 
#  
# 
#  
#  Related Topics 动态规划

"""
import bisect
import collections
import sys
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
factory = lambda: sys.maxsize


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Record the possible states of each position and number of operations to get this state.
        When we check i-th element in the arr1, dp record the possible values we can place at this position,
             and the number of operations to get to this state.
        Now, we need to build dp for (i+1)-th position, so for (i+1)-th element,
        if it's larger than the possible state from i-th state, we have two choices:
        1, keep it so no operation needs to be made.
        2, choose from arr2 a smaller element that is larger than i-th element and add one operation.
        If it's not larger than the i-th state, we definitely need to make a possible operation.
        """
        arr2 = sorted(set(arr2))
        dp = {0: -1}
        for val1 in arr1:
            next_dp = collections.defaultdict(factory)
            for cost, val in dp.items():
                if val < val1:
                    next_dp[cost] = min(next_dp[cost], val1)
                k = bisect.bisect_right(arr2, val)
                if k == len(arr2):
                    continue
                next_dp[cost + 1] = min(next_dp[cost + 1], arr2[k])
            dp = next_dp
            # print(dp)
            if not dp:
                return -1
        return min(dp.keys())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    # [dict(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]), 1],
    [dict(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]), 2],
    # [dict(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]), -1],
])
def test_solutions(kw, expected):
    assert Solution().makeArrayIncreasing(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
