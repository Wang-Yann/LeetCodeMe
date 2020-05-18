#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任
# 意数字。A 不能视为 14。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5]
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: [0,0,1,2,5]
# 输出: True 
# 
#  
# 
#  限制： 
# 
#  数组长度为 5 
# 
#  数组的数取值为 [0, 13] . 
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0:
                continue  # 跳过大小王
            ma = max(ma, num)  # 最大牌
            mi = min(mi, num)  # 最小牌
            if num in repeat:
                return False  # 若有重复，提前返回 false
            repeat.add(num)  # 添加牌至 Set
        return ma - mi < 5  # 最大牌 - 最小牌 < 5 则可构成顺子


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        cnt0 = 0
        cnt_gap = 0
        for i, v in enumerate(nums):
            if v == 0:
                cnt0 += 1
        small = cnt0
        big = cnt0 + 1
        while big < len(nums):
            if nums[small] == nums[big]:
                return False
            cnt_gap += nums[big] - nums[small] - 1
            small = big
            big += 1
        return cnt0 >= cnt_gap


@pytest.mark.parametrize("args,expected", [
    ([4, 7, 5, 9, 2], False),
    ([1, 2, 3, 4, 5], True),
    pytest.param([0, 0, 1, 2, 5], True),
])
def test_solutions(args, expected):
    assert Solution().isStraight(args) == expected
    assert Solution1().isStraight(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
