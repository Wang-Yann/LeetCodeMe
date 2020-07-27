#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 16:35:42
# @Last Modified : 2020-07-27 16:35:42
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。 
# 
#  注意: 
#  nums 数组的总和是一定在 32 位有符号整数范围之内的。 
# 
#  示例 1: 
# 
#  输入: nums = [1, -1, 5, -2, 3], k = 3
# 输出: 4 
# 解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
#  
# 
#  示例 2: 
# 
#  输入: nums = [-2, -1, 2, 1], k = 1
# 输出: 2 
# 解释: 子数组 [-1, 2] 和等于 1，且长度最长。 
# 
#  进阶: 
# 你能使时间复杂度在 O(n) 内完成此题吗? 
#  Related Topics 哈希表 
#  👍 45 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = cur_sum = 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum - k in lookup:
                ans = max(ans, i - lookup[cur_sum - k])
            if cur_sum not in lookup:
                lookup[cur_sum] = i
        # print(lookup)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, -1, 5, -2, 3], k=3), 4],
    [dict(nums=[-2, -1, 2, 1], k=1), 2],
])
def test_solutions(kw, expected):
    assert Solution().maxSubArrayLen(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
