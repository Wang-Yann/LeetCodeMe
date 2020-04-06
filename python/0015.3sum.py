#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:59:18
# @Last Modified : 2020-04-06 14:59:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     nums, result, i = sorted(nums), [], 0
#     while i < len(nums) - 2:
#         if i == 0 or nums[i] != nums[i - 1]:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#         i += 1
#     return result


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        i = 0
        while i < length - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, length - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return res

    def threeSum0(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        length = len(nums)
        res = []
        for i in range(0, length):
            v_i = nums[i]
            if v_i > 0:
                break
            for j in range(i + 1, length):
                v_j = nums[j]
                sum_ij = v_i + v_j
                if sum_ij > 0:
                    break
                for k in range(j + 1, length):
                    if sum_ij + nums[k] > 0:
                        break
                    if sum_ij + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] not in res:
                            res.append([nums[i], nums[j], nums[k]])

        return list(res)


if __name__ == '__main__':
    sol = Solution()
    sample = [-1, 0, 1, 2, -1, -4]
    sample = [1, -2, -5, -13, -10, -11, 0, -12, -11, 13, -4, 9, 8, 10, -7, 3, -9, -12, -7, 8, -2, -12, 1, -10, -15, -8, 5, 14, -7, -8, -8,
              9, -3, -6, 3, -5, -1, -11, -10, 3, -13, 1, -10, 3, -12, -10, -9, -13, -7, -1, 10, 6, -6, -12, 12, -13, -13, -6, -14, -13, -7,
              -7, 4, 6, -6, -8, 8, 8, -4, 13, -11, -1, -8, -14, 9, -5, -9, 7, -3, -1, 14, 14, 13, -7, 9, 2, -5, 12, 11, -12, 14, -11, -12,
              3, 2, -2, 3, -5, -9, 14, -14, -13, -10, -7, -12, 14, 3, -6, -1, 8, 1, -2, -1, -1, 6, -6]
    print(sol.threeSum(sample))
