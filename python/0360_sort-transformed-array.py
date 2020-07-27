#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 20:07:19
# @Last Modified : 2020-07-27 20:07:19
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个已经 排好序 的整数数组 nums 和整数 a、b、c。对于数组中的每一个数 x，计算函数值 f(x) = ax2 + bx + c，请将函数值产生
# 的数组返回。 
# 
#  要注意，返回的这个数组必须按照 升序排列，并且我们所期望的解法时间复杂度为 O(n)。 
# 
#  示例 1： 
# 
#  输入: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# 输出: [3,9,15,33]
#  
# 
#  示例 2： 
# 
#  输入: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# 输出: [-23,-5,1,7]
#  
#  Related Topics 数学 双指针 
#  👍 15 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        f = lambda x, a, b, c: a * x * x + b * x + c

        result = []
        if not nums:
            return result

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            l_val = f(nums[left], a, b, c)
            r_val = f(nums[right], a, b, c)
            if d * l_val < d * r_val:
                result.append(l_val)
                left += 1
            else:
                result.append(r_val)
                right -= 1

        return result[::d]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-4, -2, 2, 4], a=1, b=3, c=5), [3, 9, 15, 33]],
    [dict(nums=[-4, -2, 2, 4], a=-1, b=3, c=5), [-23, -5, 1, 7]],
])
def test_solutions(kw, expected):
    assert Solution().sortTransformedArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
