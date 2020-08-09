#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 12:36:50
# @Last Modified : 2020-08-09 12:36:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 nums 和一个整数 target 。 
# 
#  请你返回 非空不重叠 子数组的最大数目，且每个子数组中数字和都为 target 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [1,1,1,1,1], target = 2
# 输出：2
# 解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。
#  
# 
#  示例 2： 
# 
#  输入：nums = [-1,3,5,1,4,2,-9], target = 6
# 输出：2
# 解释：总共有 3 个子数组和为 6 。
# ([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。 
# 
#  示例 3： 
# 
#  输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：nums = [0,0,0], target = 0
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10^5 
#  -10^4 <= nums[i] <= 10^4 
#  0 <= target <= 10^6 
#  
#  Related Topics 动态规划 
#  👍 0 👎 0
	 

"""

import pytest,traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """学习了
        只需记录前一个区间的结束点，贪心选择;
        """
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        seen = set()
        res = 0
        for num in pre:
            if num in seen:
                res +=1
                seen = {num + target}
            else:
                seen.add(num + target)
        return res

# leetcode submit region end(Prohibit modification and deletion)
class Solution0:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """贪心
        """
        if not nums:
            return 0
        dic = {0 : -1}
        sum_vals = 0
        ans = 0
        last_pos = -1

        for i in range(len(nums)):
            sum_vals += nums[i]
            if sum_vals - target in dic:
                if dic[sum_vals - target] >= last_pos:
                    ans += 1
                    last_pos = i
            dic[sum_vals] = i

        return ans



class Solution1:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """Me  AC target=0 情况"""
        prefix = {0: -1}
        accu = 0
        segs = []
        for r, v in enumerate(nums):
            accu += v
            if target != 0:
                prefix[accu] = r
                if accu - target in prefix:
                    l = prefix[accu - target]
                    segs.append([l, r])
            else:
                if accu - target in prefix:
                    l = prefix[accu - target]
                    segs.append([l, r])
                prefix[accu] = r

        # print(segs)
        # 贪心选取
        segs.sort()
        N = len(segs)
        need_remove = 0
        end = float("-inf")
        for interval in sorted(segs, key=operator.itemgetter(1)):
            if interval[0] >= end:
                end = interval[1]
            else:
                need_remove += 1
        return N - need_remove

#
# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 1, 1, 1, 1], target=2), 2],

    pytest.param(dict(nums=[-1, 3, 5, 1, 4, 2, -9], target=6), 2),
    pytest.param(dict(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10), 3),
    pytest.param(dict(nums=[0, 0, 0], target=0), 3),
    pytest.param(dict(
        nums=[0, 0, -1, 0, -2, 0, 1, 0, 1, -2, -1, 2, 2, 1, -2, -2, -1, 0, 2, 2, -2, 2, 2, 0, 2, 0, -1, 1, 1, 1, 2, 1, 2, -2, -2, 0, 1, 1, 0, 2, 0, 1,
              0, 1, 2, 2, 1, 0, -1, 0, 1, 0, 2, 1, -1, 2, -2, 2, -2, 1, -1, 0, 2, -2, 0, 1, 1, -1, 1, 2, -2, -1, -2, 0, 2, -2, 0, 2, -1, -2, -1, 2,
              -1, -2, -1, 2, 1, 1, 0, 2, -1, 2, 1, -2, 0, 0, -1, 1, 1, -1, 0, -2, 1, -1, 0, -1, 2, 1, 1, 1, 2, -1, 1, 1, 0, 1, 1, 0, 0, -1, -1, 0, 0,
              -1, 2, -2, 0, 1, 1, 2, -1, 1, 1, 0, 0, -2, 0, -1, -2, 1],
        target=0), 54),
])
def test_solutions3(kwargs, expected):
    assert Solution().maxNonOverlapping(**kwargs) == expected
    assert Solution0().maxNonOverlapping(**kwargs) == expected
    assert Solution1().maxNonOverlapping(**kwargs) == expected



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])