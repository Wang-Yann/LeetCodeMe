#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。 
# 
#  注意： 
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。 
# 
#  示例: 
# 
#  
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3);
# 
# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1);
#  
#  Related Topics 蓄水池抽样

"""
import random
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self, nums: List[int]):
        self.__nums = nums

    def pick(self, target: int) -> int:
        reservoir = -1
        n = 0
        for i in range(len(self.__nums)):
            if self.__nums[i] != target:
                continue
            if random.randint(1, n + 1) == 1:
                reservoir = i
            n += 1
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    sol = Solution([1, 2, 3, 3, 3])
    assert sol.pick(3) in [2, 3, 4]
    assert sol.pick(1) == 0


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
