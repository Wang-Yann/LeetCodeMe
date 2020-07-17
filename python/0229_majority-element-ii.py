#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-16 21:44:07
# @Last Modified : 2020-04-16 21:44:07
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
#  说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: [3]
#
#  示例 2:
#
#  输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
#  Related Topics 数组
#  👍 217 👎 0

"""

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
