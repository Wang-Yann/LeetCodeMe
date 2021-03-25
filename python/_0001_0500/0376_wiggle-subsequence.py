#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。 
# 
#  例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。相反, [1,4,7,2,5] 和 [1,7,
# 4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。 
# 
#  给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。 
# 
#  示例 1: 
# 
#  输入: [1,7,4,9,2,5]
# 输出: 6 
# 解释: 整个序列均为摆动序列。
#  
# 
#  示例 2: 
# 
#  输入: [1,17,5,10,13,15,10,5,16,8]
# 输出: 7
# 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。 
# 
#  示例 3: 
# 
#  输入: [1,2,3,4,5,6,7,8,9]
# 输出: 2 
# 
#  进阶: 
# 你能否用 O(n) 时间复杂度完成此题? 
#  Related Topics 贪心算法 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        当出现升序时, 和有效的降序数量上加1, 降序同理
        """
        if len(nums) < 2:
            return len(nums)
        up, down = 1, 1
        for i in range(1, len(nums)):
            # 当出现升序时, 和**有效**的降序数量上加1
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(down, up)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 7, 4, 9, 2, 5], 6),
    ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
])
def test_solutions(args, expected):
    assert Solution().wiggleMaxLength(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
