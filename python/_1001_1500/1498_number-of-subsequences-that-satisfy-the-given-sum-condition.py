#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 19:12:52
# @Last Modified : 2020-07-10 19:12:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目。 
# 
#  由于答案可能很大，请将结果对 10^9 + 7 取余后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [3,5,6,7], target = 9
# 输出：4
# 解释：有 4 个子序列满足该条件。
# [3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
#  
# 
#  示例 2： 
# 
#  输入：nums = [3,3,6,8], target = 10
# 输出：6
# 解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6] 
# 
#  示例 3： 
# 
#  输入：nums = [2,3,3,4,6,7], target = 12
# 输出：61
# 解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
# 有效序列总数为（63 - 2 = 61）
#  
# 
#  示例 4： 
# 
#  输入：nums = [5,2,4,1,7,6,8], target = 16
# 输出：127
# 解释：所有非空子序列都满足条件 (2^7 - 1) = 127 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^6 
#  1 <= target <= 10^6 
#  
#  Related Topics 排序 Sliding Window 
#  👍 18 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        这种类型理解不好
        GOOD  TODO
        https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/solution/python-pai-xu-shuang-zhi-zhen-by-irruma/
        Sort input A first,
        For each A[i], find out the maximum A[j]
        that A[i] + A[j] <= target.

        For each elements in the subarray A[i+1] ~ A[j],
        we can pick or not pick,
        so there are 2 ^ (j - i) subsequences in total.
        So we can update res = (res + 2 ^ (j - i)) % mod.

        We don't care the original elements order,
        we only want to know the count of sub sequence.
        So we can sort the original A, and the result won't change.

        """
        mod = 10 ** 9 + 7
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, mod)
                l += 1
        return res % mod


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[3, 5, 6, 7], target=9), 4],
    [dict(nums=[3, 3, 6, 8], target=10), 6],
    [dict(nums=[2, 3, 3, 4, 6, 7], target=12), 61],
    [dict(nums=[5, 2, 4, 1, 7, 6, 8], target=16), 127],
])
def test_solutions(kw, expected):
    assert Solution().numSubseq(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
