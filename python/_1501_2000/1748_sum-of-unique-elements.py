#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 16:52:16
# @Last Modified : 2021-02-27 16:52:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。 
# 
#  请你返回 nums 中唯一元素的 和 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,2]
# 输出：4
# 解释：唯一元素为 [1,3] ，和为 4 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,1,1,1,1]
# 输出：0
# 解释：没有唯一元素，和为 0 。
#  
# 
#  示例 3 ： 
# 
#  输入：nums = [1,2,3,4,5]
# 输出：15
# 解释：唯一元素为 [1,2,3,4,5] ，和为 15 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组 哈希表 
#  👍 2 👎 0
  

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sumOfUnique(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return sum(k for k, v in counter.items() if v == 1)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 3, 2]), 4],
    [dict(nums=[1, 1, 1, 1, 1]), 0],
    [dict(nums=[1, 2, 3, 4, 5]), 15],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().sumOfUnique(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
