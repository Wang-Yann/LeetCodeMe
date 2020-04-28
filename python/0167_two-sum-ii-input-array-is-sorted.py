#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Author  : Rock
# @Date   : 4/4/20
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 2:
            return []
        for i in range(0, length - 1):
            other = target - numbers[i]
            for j in range(i + 1, length):
                if numbers[j] == other:
                    return [i + 1, j + 1]
                elif   numbers[j]>other:
                    break
        return []

    def twoSum0(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        if length < 2:
            return []
        low = 0
        high = length - 1
        while low < high:
            sum_v = numbers[low] + numbers[high]
            if sum_v == target:
                return [low + 1, high + 1]
            elif sum_v < target:
                low += 1
            else:
                high -= 1
        return []


if __name__ == '__main__':
    sol = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(numbers, target))
    print(sol.twoSum([2, 7, 9, 11, 15], 18))
    print(sol.twoSum([3, 2, 4], 6))
