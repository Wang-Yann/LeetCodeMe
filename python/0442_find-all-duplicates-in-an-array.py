#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。 
# 
#  找到所有出现两次的元素。 
# 
#  你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？ 
# 
#  示例： 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [2,3]
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        result = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                result.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return result


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
])
def test_solutions(args, expected):
    assert Solution().findDuplicates(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
