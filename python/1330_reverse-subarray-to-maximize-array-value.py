#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 20:58:20
# @Last Modified : 2020-07-05 20:58:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个整数数组 nums 。「数组值」定义为所有满足 0 <= i < nums.length-1 的 |nums[i]-nums[i+1]| 的和。 
# 
#  你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 一次 。 
# 
#  请你找到可行的最大 数组值 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [2,3,1,5,4]
# 输出：10
# 解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [2,4,9,24,2,1,10]
# 输出：68
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3*10^4 
#  -10^5 <= nums[i] <= 10^5 
#  
#  Related Topics 数组 数学 
#  👍 29 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxValueAfterReverse(self, nums: List[int]) -> int:
        """ 枚举绝对值展开后的符号
        total calculate the total sum of |A[i] - A[j]|.
        res record the value the we can improve.

        Assume the current pair is (a,b) = (A[i], A[i+1]).

        If we reverse all element from A[0] to A[i],
        we will improve abs(A[0] - b) - abs(a - b)

        If we reverse all element from A[i+1] to A[n-1],
        we will improve abs(A[n - 1] - a) - abs(a - b)

        As we iterate the whole array,
        We also record the maximum pair and the minimum pair.
        We can break these two pair and reverse all element in the middle.
        This will improve (max2 - min2) * 2
        更清晰
        https://leetcode-cn.com/problems/reverse-subarray-to-maximize-array-value/solution/tan-xin-suan-fa-suan-fa-fu-za-du-on-by-tom-chan/
        na′ =na+2maxMinus−2minAdd
        """
        N = len(nums)
        # max2 means maxValley.
        # min2 means minPeak.

        delta_list = [abs(nums[i] - nums[i - 1]) for i in range(1, N)]
        total = sum(delta_list)

        max_pair =  max([min(nums[i], nums[i-1]) for i in range(1, len(nums))]) # 获得减项的最大值
        min_pair = min([max(nums[i], nums[i-1]) for i in range(1, len(nums))])  # 获得加项的最小值
        d = 0
        for i in range(1, N):
            d = max(d, abs(nums[i] - nums[0]) - abs(nums[i] - nums[i - 1]))
            d = max(d, abs(nums[i - 1] - nums[N - 1]) - abs(nums[i] - nums[i - 1]))
        #这里没有判读a(max_pair), b(min_pair)之间的大小关系, 如果a < b 那么, 2a-2b一定小于d, 没有必要判断
        return total + max(d, (max_pair - min_pair) * 2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[2, 3, 1, 5, 4]), 10),
    pytest.param(dict(nums=[2, 4, 9, 24, 2, 1, 10]), 68),
    pytest.param(dict(nums=[2, 5, 1, 3, 4]), 11),
])
def test_solutions(kwargs, expected):
    assert Solution().maxValueAfterReverse(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
