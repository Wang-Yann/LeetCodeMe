#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。 
# 
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/ 
#  Related Topics 栈 Sliding Window

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        单调队列
        """
        if not nums or k == 0:
            return []
        deque = collections.deque()
        res = []
        for i in range(0, len(nums)):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            while i - deque[0] + 1 > k:
                deque.popleft()
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        单调队列
        """
        if not nums or k == 0:
            return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        # 形成窗口后
        res = [deque[0]]
        for i in range(k, len(nums)):
            # 删除 deque 中对应的 nums[i-1]
            if deque[0] == nums[i - k]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3
    ), [3, 3, 5, 5, 6, 7]),
])
def test_solutions(kwargs, expected):
    assert Solution().maxSlidingWindow(**kwargs) == expected
    assert Solution1().maxSlidingWindow(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
