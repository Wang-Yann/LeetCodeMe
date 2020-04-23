#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 00:28:13
# @Last Modified : 2020-04-24 00:28:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def minArray(self, numbers: List[int]) -> int:
        if not numbers:
            return
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = l + (r - l) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r-=1
        return numbers[l]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [3, 4, 5, 1, 2], [2, 2, 2, 0, 1],[3,1,1],[2,2,3]

    ]
    res = [sol.minArray(args) for args in samples]
    print(res)
