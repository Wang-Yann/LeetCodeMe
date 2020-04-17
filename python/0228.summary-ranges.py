#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:15:45
# @Last Modified : 2020-04-16 21:15:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def summaryRangesMe(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        length = len(nums)
        cur_left = cur_right = nums[0]
        for i in range(1, length):
            if nums[i] != nums[i - 1] + 1:
                ele = "{}->{}".format(cur_left, cur_right) if cur_left != cur_right else "{}".format(cur_left)
                res.append(ele)
                cur_left = nums[i]
                cur_right = nums[i]
            else:
                cur_right = nums[i]
        ele = "{}->{}".format(cur_left, cur_right) if cur_left != cur_right else "{}".format(cur_left)
        res.append(ele)
        return res

    def summaryRanges(self, nums):
        ranges = []
        if not nums:
            return ranges

        start, end = nums[0], nums[0]
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == end + 1:
                end = nums[i]
            else:
                interval = str(start)
                if start != end:
                    interval += "->" + str(end)
                ranges.append(interval)
                if i < len(nums):
                    start = end = nums[i]

        return ranges


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9]

    ]
    res = [sol.summaryRanges(x) for x in samples]
    print(res)
