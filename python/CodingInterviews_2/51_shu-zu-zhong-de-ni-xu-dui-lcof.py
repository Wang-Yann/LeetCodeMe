#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 09:38:25
# @Last Modified : 2020-04-24 09:38:25
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [7, 5, 6, 4]
    ]
    lists = [x for x in samples]
    res = [sol.reversePairs(x) for x in lists]
    print(res)
