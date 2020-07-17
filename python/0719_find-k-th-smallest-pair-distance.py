#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:34:13
# @Last Modified : 2020-05-02 14:34:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
#
#  示例 1:
#
#
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
#
#
#  提示:
#
#
#  2 <= len(nums) <= 10000.
#  0 <= nums[i] < 1000000.
#  1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#  Related Topics 堆 数组 二分查找
#  👍 99 👎 0

"""


from typing import List

import pytest


class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/solution/hei-ming-dan-zhong-de-sui-ji-shu-by-leetcode/
        我们可以使用双指针来计算出所有小于等于 guess 的距离对数目。我们维护 left 和 right，其中 right 通过循环逐渐递增，left 在每次循环中被维护，
        使得它满足 nums[right] - nums[left] <= guess 且最小。这样对于 nums[right]，以它为右端的满足距离小于等于 guess 的距离对数目即为 right - left。
        我们在循环中对这些 right - left 进行累加，就得到了所有小于等于 guess 的距离对数目。

        """

        def possible(guess):
            count, left = 0, 0
            for right, v in enumerate(nums):
                # Is there k or more pairs with distance <= guess?
                while v - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo <= hi:
            mid = (lo + hi) >> 1
            if possible(mid):
                hi = mid-1
            else:
                lo = mid + 1
        return lo


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[1, 3, 1], k=1), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().smallestDistancePair(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
