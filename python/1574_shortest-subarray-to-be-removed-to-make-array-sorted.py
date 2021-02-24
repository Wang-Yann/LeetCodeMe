#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 05:45:29
# @Last Modified : 2021-02-24 05:45:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。 
# 
#  一个子数组指的是原数组中连续的一个子序列。 
# 
#  请你返回满足题目要求的最短子数组的长度。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr = [1,2,3,10,4,2,3,5]
# 输出：3
# 解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
# 另一个正确的解为删除子数组 [3,10,4] 。 
# 
#  示例 2： 
# 
#  
# 输入：arr = [5,4,3,2,1]
# 输出：4
# 解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
#  
# 
#  示例 3： 
# 
#  
# 输入：arr = [1,2,3]
# 输出：0
# 解释：数组已经是非递减的了，我们不需要删除任何元素。
#  
# 
#  示例 4： 
# 
#  
# 输入：arr = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr.length <= 10^5 
#  0 <= arr[i] <= 10^9 
#  
#  Related Topics 数组 二分查找 
#  👍 35 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        the final remaining elements must be either: (1) solely a prefix, (2) solely a suffix or (3) a merge of the prefix and suffix
        1.Find the monotone non-decreasing prefix [a_0 <= ... a_i | ...]
        l is the index such that arr[l+1] < arr[l]
        2.Find the monotone non-decreasing suffix [... | a_j <= ... a_n]
        r is the index such that arr[r-1] > arr[r]
        3.Try to "merge 2 sorted arrays", if we can merge, update our minimum to remove.
        """
        l, r = 0, len(arr) - 1
        while l < r and arr[l + 1] >= arr[l]:
            l += 1
        if l == len(arr) - 1:
            return 0  # whole array is sorted
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        toRemove = min(len(arr) - l - 1, r)  # case (1) and (2)

        # case (3): try to merge
        for i in range(l + 1):
            if arr[i] <= arr[r]:
                toRemove = min(toRemove, r - i - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return toRemove


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr=[1, 2, 3, 10, 4, 2, 3, 5]), 3],
    [dict(arr=[5, 4, 3, 2, 1]), 4],
    [dict(arr=[1, 2, 3]), 0],
    [dict(arr=[1]), 0],
])
def test_solutions(kw, expected):
    assert Solution().findLengthOfShortestSubarray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
