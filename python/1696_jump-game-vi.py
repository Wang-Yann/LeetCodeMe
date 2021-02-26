#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 06:37:06
# @Last Modified : 2021-02-26 06:37:06
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。 
# 
#  一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, 
# i + k)] 包含 两个端点的任意位置。 
# 
#  你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。 
# 
#  请你返回你能得到的 最大得分 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,-1,-2,4,-7,3], k = 2
# 输出：7
# 解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [10,-5,-2,4,0,3], k = 3
# 输出：17
# 解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length, k <= 105 
#  -104 <= nums[i] <= 104 
#  
#  👍 32 👎 0


import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """GOOD"""
        # 维护当前最大值  方法1：最大堆  方法2:单调递减队列（队首）
        N = len(nums)
        maxHeap = []
        heapq.heappush(maxHeap, (-nums[0], 0))
        res = nums[0]

        for i in range(1, N):
            while maxHeap and i - maxHeap[0][1] > k:  # index的距离太大，以后i越来越大，top()就没用了
                heapq.heappop(maxHeap)
            res = -maxHeap[0][0] + nums[i]
            heapq.heappush(maxHeap, (-res, i))  # dp的思想
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, -1, -2, 4, -7, 3], k=2), 7],
    [dict(nums=[10, -5, -2, 4, 0, 3], k=3), 17],
    [dict(nums=[1, -5, -20, 4, -1, 3, -6, -3], k=2), 0],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxResult(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
