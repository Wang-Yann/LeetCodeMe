#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [12,345,2,6,7896]
# 输出：2
# 解释：
# 12 是 2 位数字（位数为偶数） 
# 345 是 3 位数字（位数为奇数）  
# 2 是 1 位数字（位数为奇数） 
# 6 是 1 位数字 位数为奇数） 
# 7896 是 4 位数字（位数为偶数）  
# 因此只有 12 和 7896 是位数为偶数的数字
#  
# 
#  示例 2： 
# 
#  输入：nums = [555,901,482,1771]
# 输出：1 
# 解释： 
# 只有 1771 是位数为偶数的数字。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 500 
#  1 <= nums[i] <= 10^5 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(num)) % 2 == 0 for num in nums)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[12, 345, 2, 6, 7896]), 2],
    [dict(nums=[555, 901, 482, 1771]), 1],
])
def test_solutions(kw, expected):
    assert Solution().findNumbers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
