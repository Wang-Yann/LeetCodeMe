#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 20:19:36
# @Last Modified : 2020-07-13 20:19:36
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？ 
# 
#  注意：本题相对书上原题稍作改动 
# 
#  示例 1： 
# 
#  输入：[3,0,1]
# 输出：2 
# 
#  
# 
#  示例 2： 
# 
#  输入：[9,6,4,2,3,5,7,0,1]
# 输出：8
#  
#  Related Topics 位运算 数组 数学 
#  👍 18 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i, num in enumerate(nums):
            res ^= i
            res ^= num
        res ^= N
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [3, 0, 1]
            , 2),
    pytest.param([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
])
def test_solutions(args, expected):
    assert Solution().missingNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
