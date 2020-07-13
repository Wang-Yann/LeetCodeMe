#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:34:01
# @Last Modified : 2020-07-13 14:34:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8
# , 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。 
# 
#  示例: 
# 
#  输入: [5, 3, 1, 2, 3]
# 输出: [5, 1, 3, 2, 3]
#  
# 
#  提示： 
# 
#  
#  nums.length <= 10000 
#  
#  👍 12 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if i % 2 == 0:
                if nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            else:
                if nums[i] > nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[5, 3, 1, 2, 3]), [5, 1, 3, 2, 3]],
])
def test_solutions(kw, expected):
    Solution().wiggleSort(**kw)
    assert kw["nums"] == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
