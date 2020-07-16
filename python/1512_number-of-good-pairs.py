#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 23:35:26
# @Last Modified : 2020-07-16 23:35:26
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给你一个整数数组 nums 。 
# 
#  如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。 
# 
#  返回好数对的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,3,1,1,3]
# 输出：4
# 解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,1,1,1]
# 输出：6
# 解释：数组中的每组数字都是好数对 
# 
#  示例 3： 
# 
#  输入：nums = [1,2,3]
# 输出：0
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
#  Related Topics 数组 哈希表 数学 
#  👍 6 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        """AC"""
        counter = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for v in counter.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 2, 3, 1, 1, 3]), 4],

    pytest.param(dict(nums=[1, 1, 1, 1]), 6),
    pytest.param(dict(nums=[1, 2, 3]), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().numIdenticalPairs(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
