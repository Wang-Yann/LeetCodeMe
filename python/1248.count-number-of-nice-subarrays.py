#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 09:44:58
# @Last Modified : 2020-04-21 09:44:58
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from typing import List


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
        print("Pre Array", cnt)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, 1, 2, 1, 1], 3),
        ([2, 4, 6], 1),
        ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),

    ]
    lists = [x for x in samples]
    res = [sol.numberOfSubarrays(*x) for x in lists]
    print(res)
