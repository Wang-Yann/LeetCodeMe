#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 10:41:06
# @Last Modified : 2020-07-13 10:41:06
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找
# 出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。 
# 
#  示例1: 
# 
#   输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0
#  
# 
#  示例2: 
# 
#   输入：nums = [1, 1, 1]
#  输出：1
#  
# 
#  提示: 
# 
#  
#  nums长度在[1, 1000000]之间 
#  
#  Related Topics 数组 二分查找 
#  👍 17 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        def search(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) >> 1
            if nums[mid] == mid:
                left = search(lo, min(mid - 1, nums[mid]))
                if left != -1:
                    return left
                else:
                    return mid
            else:
                left = search(lo, min(mid - 1, nums[mid]))
                if left >= 0:
                    return left
                right = search(max(mid + 1, nums[mid]), hi)
                return right

        return search(0, len(nums) - 1)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[0, 2, 3, 4, 5]), 0],
    [dict(nums=[1, 1, 1]), 1],
    [dict(nums=[0, 0, 2]), 0],
    [dict(nums=[0, 1, 2]), 0],
])
def test_solutions(kw, expected):
    assert Solution().findMagicIndex(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
