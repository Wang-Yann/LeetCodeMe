#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 10:45:56
# @Last Modified : 2020-08-04 10:45:56
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 A，返回满足下面条件的 非空、连续 子数组的数目： 
# 
#  子数组中，最左侧的元素不大于其他元素。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,4,2,5,3]
# 输出：11
# 解释：有 11 个有效子数组，分别是：[1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[
# 1,4,2,5,3] 。
#  
# 
#  示例 2： 
# 
#  输入：[3,2,1]
# 输出：3
# 解释：有 3 个有效子数组，分别是：[3],[2],[1] 。
#  
# 
#  示例 3： 
# 
#  输入：[2,2,2]
# 输出：6
# 解释：有 6 个有效子数组，分别为是：[2],[2],[2],[2,2],[2,2],[2,2,2] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 50000 
#  0 <= A[i] <= 100000 
#  
#  Related Topics 栈 
#  👍 18 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        """GOOD"""
        stack = []
        ans = 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            ans += len(stack)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([1, 4, 2, 5, 3], 11),
    ([3, 2, 1], 3),
    ([2, 2, 2], 6),
])
def test_solutions(args, expected):
    assert Solution().validSubarrays(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
