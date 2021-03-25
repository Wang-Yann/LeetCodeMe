#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 12:46:13
# @Last Modified : 2020-04-06 12:46:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [3,2,3]
# 输出: 3
#
#  示例 2:
#
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#  Related Topics 位运算 数组 分治算法
#  👍 667 👎 0

"""

from collections import Counter
from typing import List

import pytest


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)
        return max(res.items(), key=lambda x: x[1])[0]


@pytest.mark.parametrize("args,expected", [
    ([2, 2, 1, 1, 1, 2, 2], 2)
])
def test_solutions(args, expected):
    assert Solution().majorityElement(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
