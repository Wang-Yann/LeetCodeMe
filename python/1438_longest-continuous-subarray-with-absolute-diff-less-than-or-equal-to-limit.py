#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limi
# t 。 
# 
#  如果不存在满足条件的子数组，则返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [8,2,4,7], limit = 4
# 输出：2 
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4. 
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4. 
# 因此，满足题意的最长子数组的长度为 2 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4 
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
#  
# 
#  示例 3： 
# 
#  输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  1 <= nums[i] <= 10^9 
#  0 <= limit <= 10^9 
#  
#  Related Topics 数组 Sliding Window

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        降序队列队首是最大值，升序队列队首是最小值
        需要java中TreeSet　或　C++ multiSet
        """
        max_dq, min_dq = collections.deque(), collections.deque()
        left, res = 0, 0
        for right, num in enumerate(nums):
            # 单调栈　递减
            while max_dq and nums[max_dq[-1]] <= num:
                max_dq.pop()
            max_dq.append(right)
            # 单调栈　递增
            while min_dq and nums[min_dq[-1]] >= num:
                min_dq.pop()
            min_dq.append(right)
            # print("Min_dq,Max_dq",min_dq,max_dq)
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            res = max(res, right - left + 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[8, 2, 4, 7], limit=4), 2],
    [dict(nums=[10, 1, 2, 4, 7, 2], limit=5), 4],
    [dict(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0), 3],
    [dict(nums=[1] * 20000 + [0], limit=3), 20001],
])
def test_solutions(kw, expected):
    assert Solution().longestSubarray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
