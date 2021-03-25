#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 19:39:17
# @Last Modified : 2021-02-27 19:39:17
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums ，其中 nums[i] 表示第 i 个袋子里球的数目。同时给你一个整数 maxOperations 。 
# 
#  你可以进行如下操作至多 maxOperations 次： 
# 
#  
#  选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 正整数 个球。
# 
#  
#  比方说，一个袋子里有 5 个球，你可以把它们分到两个新袋子里，分别有 1 个和 4 个球，或者分别有 2 个和 3 个球。 
#  
#  
#  
# 
#  你的开销是单个袋子里球数目的 最大值 ，你想要 最小化 开销。 
# 
#  请你返回进行上述操作后的最小开销。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [9], maxOperations = 2
# 输出：3
# 解释：
# - 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
# - 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
# 装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,4,8,2], maxOperations = 4
# 输出：2
# 解释：
# - 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
# - 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
# 装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,17], maxOperations = 2
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  1 <= maxOperations, nums[i] <= 109 
#  
#  Related Topics 堆 二分查找 
#  👍 24 👎 0
  

"""

from typing import List

import pytest


#
# For example, the mid = 3,
# A[i] = 2, we split it into [2], and operations = 0
# A[i] = 3, we split it into [3], and operations = 0
# A[i] = 4, we split it into [3,1], and operations = 1
# A[i] = 5, we split it into [3,2], and operations = 1
# A[i] = 6, we split it into [3,3], and operations = 1
# A[i] = 7, we split it into [3,3,1], and operations = 2
#
# The number of operation we need is (a - 1) / mid


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """经典场景"""

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check(mid_val):
            return sum((x - 1) // mid_val for x in nums) > maxOperations

        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[9], maxOperations=2), 3],
    [dict(nums=[2, 4, 8, 2], maxOperations=4), 2],
    [dict(nums=[7, 17], maxOperations=2), 7],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minimumSize(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
