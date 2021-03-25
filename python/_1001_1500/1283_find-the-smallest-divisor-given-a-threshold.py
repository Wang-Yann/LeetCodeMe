#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个正整数 threshold ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。 
# 
#  请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。 
# 
#  每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。 
# 
#  题目保证一定有解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,5,9], threshold = 6
# 输出：5
# 解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
# 如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,3,5,7,11], threshold = 11
# 输出：3
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [19], threshold = 5
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 5 * 10^4 
#  1 <= nums[i] <= 10^6 
#  nums.length <= threshold <= 10^6 
#  
#  Related Topics 二分查找

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """领会边界"""
        l, r = 1, max(nums)

        def check(d):
            return sum(math.ceil(x / d) for x in nums) <= threshold

        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 5, 9], threshold=6), 5],
    [dict(nums=[2, 3, 5, 7, 11], threshold=11), 3],
    [dict(nums=[19], threshold=5), 4],
])
def test_solutions(kw, expected):
    assert Solution().smallestDivisor(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
