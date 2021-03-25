#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 16:39:50
# @Last Modified : 2020-07-22 16:39:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个长度为 n 的整数数组和一个目标值 target，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三
# 元组 i, j, k 个数（0 <= i < j < k < n）。 
# 
#  示例： 
# 
#  输入: nums = [-2,0,1,3], target = 2
# 输出: 2 
# 解释: 因为一共有两个三元组满足累加和小于 2:
#      [-2,0,1]
#      [-2,0,3]
#  
# 
#  进阶：是否能在 O(n2) 的时间复杂度内解决？ 
#  Related Topics 数组 双指针 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        k = 2
        while k < N:
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    ans += j - i
                    i += 1
                else:
                    j -= 1
            k += 1
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[-2, 0, 1, 3], target=2), 2],
])
def test_solutions(kw, expected):
    assert Solution().threeSumSmaller(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
