#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 23:37:42
# @Last Modified : 2020-07-16 23:37:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0


# 给你一个数组 nums ，每次操作你可以选择 nums 中的任意一个元素并将它改成任意值。 
# 
#  请你返回三次操作后， nums 中最大值与最小值的差的最小值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [5,3,2,4]
# 输出：0
# 解释：将数组 [5,3,2,4] 变成 [2,2,2,2].
# 最大值与最小值的差为 2-2 = 0 。 
# 
#  示例 2： 
# 
#  输入：nums = [1,5,0,10,14]
# 输出：1
# 解释：将数组 [1,5,0,10,14] 变成 [1,1,0,1,1] 。
# 最大值与最小值的差为 1-0 = 1 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [6,6,0,1,1,4,6]
# 输出：2
#  
# 
#  示例 4： 
# 
#  输入：nums = [1,5,6,14,15]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^9 <= nums[i] <= 10^9 
#  
#  Related Topics 排序 数组 
#  👍 2 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDifference(self, nums: List[int]) -> int:
        """AC"""
        nums.sort()
        N = len(nums)
        if N <= 4:
            return 0
        candidates = (
            abs(nums[0] - nums[N - 4]),
            abs(nums[3] - nums[N - 1]),
            abs(nums[2] - nums[N - 2]),
            abs(nums[1] - nums[N - 3]),

        )
        return min(candidates)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[5, 3, 2, 4]), 0],
    pytest.param(dict(nums=[1, 5, 0, 10, 14]), 1),
    pytest.param(dict(nums=[6, 6, 0, 1, 1, 4, 6]), 2),
    pytest.param(dict(nums=[1, 5, 6, 14, 15]), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().minDifference(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
