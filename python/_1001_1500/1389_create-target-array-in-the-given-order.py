#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组： 
# 
#  
#  目标数组 target 最初为空。 
#  按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。 
#  重复上一步，直到在 nums 和 index 中都没有要读取的元素。 
#  
# 
#  请你返回目标数组。 
# 
#  题目保证数字插入位置总是存在。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
# 输出：[0,4,1,3,2]
# 解释：
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
# 输出：[0,1,2,3,4]
# 解释：
# nums       index     target
# 1            0        [1]
# 2            1        [1,2]
# 3            2        [1,2,3]
# 4            3        [1,2,3,4]
# 0            0        [0,1,2,3,4]
#  
# 
#  示例 3： 
# 
#  输入：nums = [1], index = [0]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length, index.length <= 100 
#  nums.length == index.length 
#  0 <= nums[i] <= 100 
#  0 <= index[i] <= i 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for num, idx in zip(nums, index):
            ans.insert(idx, num)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]), [0, 4, 1, 3, 2]],
    [dict(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]), [0, 1, 2, 3, 4]],
    [dict(nums=[1], index=[0]), [1]],
])
def test_solutions(kw, expected):
    assert Solution().createTargetArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
