#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 nums，请你将该数组升序排列。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000 
#  
# 

"""
import random
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        def randomized_partition(l, r):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            i = l - 1
            for j in range(l, r):
                if nums[j] < nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        def randomized_quicksort(l, r):
            if r - l <= 0:
                return
            mid = randomized_partition(l, r)
            randomized_quicksort(l, mid - 1)
            randomized_quicksort(mid + 1, r)

        randomized_quicksort(0, len(nums) - 1)
        return nums


# leetcode submit region end(Prohibit modification and deletion)

class SolutionMerge:

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(l, r):
            if l == r:
                return
            mid = (l + r) >> 1
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            tmp = []
            i, j = l, mid + 1
            while i <= mid or j <= r:
                if i > mid or (j <= r and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[l:r + 1] = tmp

        merge_sort(0, len(nums) - 1)
        return nums


@pytest.mark.parametrize("args,expected", [
    ([5, 2, 3, 1], [1, 2, 3, 5]),
    ([3, -1], [-1, 3]),
    ([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1], [-7, -5, -4, -1, -1, 0, 0, 4, 7, 9]),
    pytest.param([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
])
def test_solutions(args, expected):
    assert Solution().sortArray(args[:]) == expected
    assert SolutionMerge().sortArray(args[:]) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
