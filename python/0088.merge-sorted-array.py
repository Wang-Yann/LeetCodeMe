#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-05 12:19:52
# @Last Modified : 2020-04-05 12:19:52
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def mergeArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = 0, 0
        idx_total = 0
        ret = [0] * (m + n)
        while idx1 <= m - 1 and idx2 <= n - 1:
            if nums1[idx1] > nums2[idx2]:
                ret[idx_total] = nums2[idx2]
                idx2 += 1
            else:
                ret[idx_total] = nums1[idx1]
                idx1 += 1
            idx_total += 1
        while idx1 <= m - 1:
            ret[idx_total] = nums1[idx1]
            idx1 += 1
            idx_total += 1

        while idx2 <= n - 1:
            ret[idx_total] = nums2[idx2]
            idx2 += 1
            idx_total += 1
        return ret

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        idx_total = m + n - 1
        while idx_total >= 0 and idx2 >= 0 and idx1>=0:
            if nums2[idx2] >= nums1[idx1]:
                nums1[idx_total] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[idx_total] = nums1[idx1]
                idx1 -= 1
            idx_total -= 1
        # print("---", nums1, idx1, idx2, idx_total)
        while idx2 >= 0:
            nums1[idx_total] = nums2[idx2]
            idx_total -= 1
            idx2 -= 1


if __name__ == '__main__':
    sol = Solution()
    nums0 = [1, 2, 3, 0, 0, 0]
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [4, 5, 6, 0, 0, 0]
    nums3 = [1, 0]
    nums4 = [4, 0, 0, 0, 0, 0]
    print(sol.merge(nums0, 3, [4, 5, 6], 3))
    print(sol.merge(nums1, 3, [2, 5, 6], 3))
    print(sol.merge(nums2, 3, [1, 2, 3], 3))
    print(sol.merge(nums3, 1, [2], 1))
    print(sol.merge(nums4, 1, [1, 2, 3, 5, 6], 5))
    # print(sol.mergeArray(nums4, 1, [1, 2, 3,5,6], 5))
    print(nums0)
    print(nums1)
    print(nums2)
    print(nums3)
    print(nums4)
