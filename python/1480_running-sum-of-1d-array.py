#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 16:07:48
# @Last Modified : 2020-07-10 16:07:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。 
# 
#  请返回 nums 的动态和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,4]
# 输出：[1,3,6,10]
# 解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。 
# 
#  示例 2： 
# 
#  输入：nums = [1,1,1,1,1]
# 输出：[1,2,3,4,5]
# 解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。 
# 
#  示例 3： 
# 
#  输入：nums = [3,1,2,10,1]
# 输出：[3,4,6,16,17]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  -10^6 <= nums[i] <= 10^6 
#  
#  Related Topics 数组 
#  👍 8 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]
        return nums


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3, 4]), [1, 3, 6, 10]],
    [dict(nums=[1, 1, 1, 1, 1]), [1, 2, 3, 4, 5]],
    [dict(nums=[3, 1, 2, 10, 1]), [3, 4, 6, 16, 17]],
])
def test_solutions(kw, expected):
    assert Solution().runningSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
