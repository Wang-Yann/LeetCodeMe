#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 23:13:31
# @Last Modified : 2020-04-22 23:13:31
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。
#
#  示例 1：
#
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
#
#
#
#  限制：
#
#  2 <= n <= 100000
#  Related Topics 数组 哈希表
#  👍 112 👎 0


from typing import List


class Solution:

    def findRepeatNumber(self, nums: List[int]) -> int:
        hash_set = set()
        for v in nums:
            if v in hash_set:
                return v
            hash_set.add(v)

class Solution1:

    def findRepeatNumber(self, nums: List[int]) -> int:
        length =  len(nums)
        if not length:
            return None
        for i in range(length):
            if not 0<=nums[i]<=length-1:return None
            while i!=nums[i]:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                v=nums[i]
                nums[i],nums[v]  = nums[v],nums[i]



if __name__ == '__main__':
    sol = Solution()
    samples = [
        [2, 3, 1, 0, 2, 5, 3]

    ]
    res = [sol.findRepeatNumber(x) for x in samples]
    print(res)
