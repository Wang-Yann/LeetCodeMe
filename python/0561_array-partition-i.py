#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 
# 的 min(ai, bi) 总和最大。 
# 
#  示例 1: 
# 
#  
# 输入: [1,4,3,2]
# 
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
#  
# 
#  提示: 
# 
#  
#  n 是正整数,范围在 [1, 10000]. 
#  数组中的元素范围在 [-10000, 10000]. 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(v for i, v in enumerate(nums) if i % 2 == 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 4, 3, 2], 4),
])
def test_solutions(args, expected):
    assert Solution().arrayPairSum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
