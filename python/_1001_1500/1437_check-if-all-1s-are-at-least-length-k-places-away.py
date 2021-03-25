#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 21:52:28
# @Last Modified : 2020-07-09 21:52:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个由若干 0 和 1 组成的数组 nums 以及整数 k。如果所有 1 都至少相隔 k 个元素，则返回 True ；否则，返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：nums = [1,0,0,0,1,0,0,1], k = 2
# 输出：true
# 解释：每个 1 都至少相隔 2 个元素。 
# 
#  示例 2： 
# 
#  
# 
#  输入：nums = [1,0,0,1,0,1], k = 2
# 输出：false
# 解释：第二个 1 和第三个 1 之间只隔了 1 个元素。 
# 
#  示例 3： 
# 
#  输入：nums = [1,1,1,1,1], k = 0
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：nums = [0,1,0,1], k = 1
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  0 <= k <= nums.length 
#  nums[i] 的值为 0 或 1 
#  
#  Related Topics 数组 
#  👍 2 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        """
        AC
        """
        prev_pos = -0x80000000
        for i, v in enumerate(nums):
            if v == 1:
                if i - prev_pos - 1 < k:
                    return False
                prev_pos = i
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2), True],
    [dict(nums=[1, 0, 0, 1, 0, 1], k=2), False],
    [dict(nums=[1, 1, 1, 1, 1], k=0), True],
    [dict(nums=[0, 1, 0, 1], k=1), True],

])
def test_solutions(kwargs, expected):
    assert Solution().kLengthApart(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
