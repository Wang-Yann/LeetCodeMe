#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。 
# 
#  示例 : 
# 
#  输入: [1,2,1,3,2,5]
# 输出: [3,5] 
# 
#  注意： 
# 
#  
#  结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。 
#  你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？ 
#  
#  Related Topics 位运算

"""

import functools
import operator
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        x & (-x) 是保留位中最右边 1 ，且将其余的 1 设位 0 的方法
        """
        bitmask = functools.reduce(operator.xor, nums)
        # rightmost 1-bit diff between x and y
        diff = bitmask & -bitmask
        res = [0, 0]
        for v in nums:
            # bitmask which will contain only x
            res[bool(v & diff)] ^= v
        return res
        # x = 0
        # for num in nums:
        #     # bitmask which will contain only x
        #     if num & diff:
        #         x ^= num
        #
        # return [x, bitmask^x]



# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 1, 3, 2, 5], [3, 5])
])
def test_solutions(args, expected):
    assert sorted(Solution().singleNumber(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
