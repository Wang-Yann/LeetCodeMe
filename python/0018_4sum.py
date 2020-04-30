#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 14:59:18
# @Last Modified : 2020-04-06 14:59:18
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List


#

class Solution:

    def fourSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #  i j k
        nums.sort()
        length = len(nums)
        res = []
        i = 0
        while i < length - 3:
            if i and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            while j < length - 2:
                if j != i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                v_sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] < v_sum:
                        left += 1
                    elif nums[left] + nums[right] > v_sum:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left, right = left + 1, right - 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                j += 1
            i += 1
        return res


# Space: O(n^2)
class Solution3(object):
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, result, lookup = sorted(nums), [], collections.defaultdict(list)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                lookup[nums[i] + nums[j]].append([i, j])

        for i in lookup.keys():
            if target - i in lookup:
                for x in lookup[i]:
                    for y in lookup[target - i]:
                        [a, b], [c, d] = x, y
                        if a is not c and a is not d and \
                                b is not c and b is not d:
                            quad = sorted([nums[a], nums[b], nums[c], nums[d]])
                            if quad not in result:
                                result.append(quad)
        return sorted(result)


if __name__ == '__main__':
    sol = Solution3()
    sample = [-1, 0, 1, 2, -1, -4]
    sample1 = [1, 0, -1, 0, -2, 2]
    print(sol.fourSum(sample, 0))
    print(sol.fourSum(sample1, 0))
