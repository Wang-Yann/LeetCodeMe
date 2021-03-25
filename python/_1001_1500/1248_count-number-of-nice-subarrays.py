#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 09:44:58
# @Last Modified : 2020-04-21 09:44:58
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给你一个整数数组 nums 和一个整数 k。
#
#  如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
#
#  请返回这个数组中「优美子数组」的数目。
#
#
#
#  示例 1：
#
#  输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
#
#
#  示例 2：
#
#  输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
#
#
#  示例 3：
#
#  输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  1 <= nums[i] <= 10^5
#  1 <= k <= nums.length
#
#  Related Topics 双指针
#  👍 121 👎 0

from typing import List

import pytest


class Solution0:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums, k):
            """GOOD"""
            result, left, count = 0, 0, 0
            for right in range(len(nums)):
                count += nums[right] % 2
                while count > k:
                    count -= nums[left] % 2
                    left += 1
                result += right - left + 1
            return result

        return atMost(nums, k) - atMost(nums, k - 1)


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """ 前缀和 + 差分

        https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/tong-ji-you-mei-zi-shu-zu-by-leetcode-solution/
        考虑以 i 结尾的「优美子数组」个数，我们需要统计符合条件的下标 jj 的个数,
        其中  0≤j≤i 且 [j..i] 这个子数组里的奇数个数恰好为 k

        pre[i] 为 [0..i] 中奇数的个数
        [j..i] 这个子数组里的奇数个数恰好为 k这个条件我们可以转化为
        pre[i]−pre[j−1]==k
        我们考虑以 i 结尾的「优美子数组」个数时只要统计有多少个奇数个数为 pre[i]−k 的 pre[j] 即可。
        我们只要建立频次数组 cnt 记录 pre[i] 出现的次数，从左往右边更新 cnt 边计算答案

        """
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
        # print("Pre Array", cnt)
        return ans


@pytest.mark.parametrize("args,expected", [
    [([1, 1, 2, 1, 1], 3), 2],
    [([2, 4, 6], 1), 0],
    [([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2), 16],
])
def test_solutions(args, expected):
    assert Solution().numberOfSubarrays(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
