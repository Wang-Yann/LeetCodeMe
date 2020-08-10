#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 09:38:25
# @Last Modified : 2020-04-24 09:38:25
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#
#
#  示例 1:
#
#  输入: [7,5,6,4]
# 输出: 5
#
#
#
#  限制：
#
#  0 <= 数组长度 <= 50000
#  👍 205 👎 0


from typing import List

import pytest


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        copy = []
        copy.extend(nums)

        def helper(start, end):
            if start == end:
                copy[start] = nums[start]
                return 0
            mid = (end + start) // 2
            left = helper(start, mid)
            right = helper(mid + 1, end)

            i = mid  # 前半段最后
            j = end  # 后半段最后
            idx_copy = end
            cnt = 0
            while i >= start and j >= mid + 1:
                if nums[i] > nums[j]:
                    copy[idx_copy] = nums[i]
                    idx_copy -= 1
                    i -= 1
                    cnt += j - mid
                else:
                    copy[idx_copy] = nums[j]
                    idx_copy -= 1
                    j -= 1
            while i >= start:
                copy[idx_copy] = nums[i]
                idx_copy -= 1
                i -= 1
            while j >= mid + 1:
                copy[idx_copy] = nums[j]
                j -= 1
                idx_copy -= 1
            # TODO 重点,书上错误;需要将nums对应块排序
            # nums[start:end+1] = copy[start:end+1]
            for k in range(start, end + 1):
                nums[k] = copy[k]
            return left + right + cnt

        count = helper(0, len(nums) - 1)
        # print("End:", nums, copy)
        return count


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[7, 5, 6, 4]), 5],
])
def test_solutions(kw, expected):
    assert Solution().reversePairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
