#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 03:31:22
# @Last Modified : 2021-02-26 03:31:22
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个 非递减 有序整数数组 nums 。 
# 
#  请你建立并返回一个整数数组 result，它跟 nums 长度相同，且result[i] 等于 nums[i] 与数组中所有其他元素差的绝对值之和。 
# 
#  换句话说， result[i] 等于 sum(|nums[i]-nums[j]|) ，其中 0 <= j < nums.length 且 j != i （
# 下标从 0 开始）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,5]
# 输出：[4,3,5]
# 解释：假设数组下标从 0 开始，那么
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,4,6,8,10]
# 输出：[24,15,13,15,21]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 105 
#  1 <= nums[i] <= nums[i + 1] <= 104 
#  
#  Related Topics 贪心算法 数学 
#  👍 12 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        """
        前缀和
        res[i] = (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i - 1])      
    + (nums[i] - nums[i]) + (nums[i + 1] - nums[i]) + (nums[i + 2] - nums[i]) + ... + (nums[n - 1] - nums[i])
    after simplification:


        res[i] = i * nums[i] - (nums[0] + ... + nums[i - 1])  <--- absolute difference of nums[i] with first i numbers
        + (nums[i + 1] + ... + nums[n]) - (n - i) * nums[i]  <--- absolute difference of nums[i] with last n - i numbers
        """
        N, prefix_sum, res = len(nums), [0], []
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        for i, num in enumerate(nums):
            res.append(i * num - prefix_sum[i] + (prefix_sum[N] - prefix_sum[i] - (N - i) * num))
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[2, 3, 5]), [4, 3, 5]],
    [dict(nums=[1, 4, 6, 8, 10]), [24, 15, 13, 15, 21]],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().getSumAbsoluteDifferences(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
