#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 打乱一个没有重复元素的数组。 
# 
#  
# 
#  示例: 
# 
#  // 以数字集合 1, 2 和 3 初始化数组。
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
# solution.shuffle();
# 
# // 重设数组到它的初始状态[1,2,3]。
# solution.reset();
# 
# // 随机返回数组[1,2,3]打乱后的结果。
# solution.shuffle();
#  
# 

"""
import random
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self, nums: List[int]):
        self.__list = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.__list

    def shuffleSimple(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        data_list = self.__list.copy()
        # random.seed(int(time.time()))
        random.shuffle(data_list)
        return data_list

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = list(self.__list)
        for i in range(len(self.__list)):
            j = random.randint(i, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    obj = Solution([1, 2, 3, 4, 5, 6])
    param_1 = obj.reset()
    param_2 = obj.shuffleSimple()
    param_3 = obj.shuffle()
    # print(param_2, param_3)
    assert param_2


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
