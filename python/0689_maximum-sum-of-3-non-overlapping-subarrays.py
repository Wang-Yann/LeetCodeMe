#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定数组 nums 由正整数组成，找到三个互不重叠的子数组的最大和。 
# 
#  每个子数组的长度为k，我们要使这3*k个项的和最大化。 
# 
#  返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。 
# 
#  示例: 
# 
#  
# 输入: [1,2,1,2,6,7,5,1], 2
# 输出: [0, 3, 5]
# 解释: 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
# 我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
#  
# 
#  注意: 
# 
#  
#  nums.length的范围在[1, 20000]之间。 
#  nums[i]的范围在[1, 65535]之间。 
#  k的范围在[1, floor(nums.length / 3)]之间。 
#  
#  Related Topics 数组 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        题意理解费劲　
        https://www.jiuzhang.com/solution/maximum-sum-of-3-non-overlapping-subarrays/#tag-highlight-lang-python
        三滑动窗口 GOOD TODO
        """
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestTwoSeq = [0, k]
        bestThreeSeq = [0, k, k * 2]

        # Sums of each window
        seqSum = sum(nums[:k])
        seqTwoSum = sum(nums[k:2 * k])
        seqThreeSum = sum(nums[2 * k:3 * k])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        seqIndex = 1
        twoSeqIndex = k + 1
        threeSeqIndex = k * 2 + 1
        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]

            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestTwoSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestThreeSeq = bestTwoSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1

        return bestThreeSeq


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (([1, 2, 1, 2, 6, 7, 5, 1], 2), [0, 3, 5])
])
def test_solutions(args, expected):
    assert Solution().maxSumOfThreeSubarrays(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
