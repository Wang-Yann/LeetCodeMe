#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。 
# 
#  说明： 
# 
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
# 
#  示例 1: 
# 
#  输入: [2,2,3,2]
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: [0,1,0,1,0,1,99]
# 输出: 99 
#  Related Topics 位运算

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums)) * 3 - sum(nums)) // 2


@pytest.mark.parametrize("args,expected", [
    ([2, 2, 3, 2], 3),
    pytest.param([0, 1, 0, 1, 0, 1, 99], 99),
])
def test_solutions(args, expected):
    assert Solution().singleNumber(args) == expected
    assert Solution1().singleNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
