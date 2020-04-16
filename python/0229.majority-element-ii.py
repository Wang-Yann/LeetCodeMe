#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:44:07
# @Last Modified : 2020-04-16 21:44:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i[0] for i in collections.Counter(nums).items() if i[1] > len(nums) / 3]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        [1, 1, 1, 3, 3, 2, 2, 2],
        [3, 2, 3]
    ]
    res = [sol.majorityElement(x) for x in samples]
    print(res)
