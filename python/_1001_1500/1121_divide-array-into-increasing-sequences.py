#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 17:56:00
# @Last Modified : 2020-08-04 17:56:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 非递减 的正整数数组 nums 和整数 K，判断该数组是否可以被分成一个或几个 长度至少 为 K 的 不相交的递增子序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,2,2,3,3,4,4], K = 3
# 输出：true
# 解释：
# 该数组可以分成两个子序列 [1,2,3,4] 和 [2,3,4]，每个子序列的长度都至少是 3。
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,6,6,7,8], K = 3
# 输出：false
# 解释：
# 没有办法根据条件来划分数组。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= K <= nums.length 
#  1 <= nums[i] <= 10^5 
#  
#  Related Topics 数学 
#  👍 16 👎 0

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        """
        因为所有数字出现次数最多为 t，其他数字出现的次数一定小于等于 t。那么他们一定可以分配到 n 个不同的子序列中。
        如果 n 无限大很有可能每个子序列的数量小于 k，所以 n 应该越小越好。当 n = t 的时候可以取到最小值，
        又因为题目要求长度至少为 k，此时长度的总和为 t * k，此时只需要保证这个长度小于等于整个数组的长度，就能满足题目的要求

        """
        curr, max_count = 1, 1
        for i in range(1, len(nums)):
            curr = 1 if nums[i - 1] < nums[i] else curr + 1
            max_count = max(max_count, curr)
        return K * max_count <= len(nums)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        return K * max(collections.Counter(nums).values()) <= len(nums)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 2, 3, 3, 4, 4], K=3), True],
    [dict(nums=[5, 6, 6, 7, 8], K=3), False],
])
def test_solutions(kw, expected):
    assert Solution().canDivideIntoSubsequences(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
