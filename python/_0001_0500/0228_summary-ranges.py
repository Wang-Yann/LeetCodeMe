#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:15:45
# @Last Modified : 2020-04-16 21:15:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
#  示例 1:
#
#  输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#
#  示例 2:
#
#  输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#  Related Topics 数组
#  👍 53 👎 0

"""

from typing import List

import pytest


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


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
    ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
])
def test_solutions(args, expected):
    assert Solution().summaryRanges(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
