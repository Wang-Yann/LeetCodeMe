#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你打算利用空闲时间来做兼职工作赚些零花钱。 
# 
#  这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。 
# 
#  给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。 
# 
#  注意，时间上出现重叠的 2 份工作不能同时进行。 
# 
#  如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# 输出：120
# 解释：
# 我们选出第 1 份和第 4 份工作， 
# 时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60
# ]
# 输出：150
# 解释：
# 我们选择第 1，4，5 份工作。 
# 共获得报酬 150 = 20 + 70 + 60。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# 输出：6
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
#  1 <= startTime[i] < endTime[i] <= 10^9 
#  1 <= profit[i] <= 10^4 
#  
#  Related Topics 排序 二分查找 动态规划

"""

import bisect
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        GOOD
        H是个最小堆，里面会有2种数据
        (startTime, 1, endTime, profit)的工作和
        (endTime, 0, profits)的结余（姑且这么叫吧）
        一开始时收入为0
        当H不为空时，提出其中的最小值：
        如果是工作，那么将endTime，当前最大收入加上本次收入记录到堆里面。
        如果是结余，那么不会有开始时间比其更小的工作，说明到这个时间为止，最大收入是profits，将其记录为res。
        """
        min_heap = list(zip(startTime, endTime, profit))
        heapq.heapify(min_heap)
        res = 0
        while min_heap:
            s, e, p = heapq.heappop(min_heap)
            if s < e:
                heapq.heappush(min_heap, (e, 0, res + p))
            else:
                res = max(res, p)
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
           https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
           If we don't do this job, nothing will be changed.
            If we do this job, binary search in the dp to find the largest profit we can make before start time s.
            So we also know the maximum current profit that we can make doing this job.
        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect_left(dp, [s + 1, 0]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        # print(dp)
        return dp[-1][1]


@pytest.mark.parametrize("kw,expected", [
    [dict(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]), 120],
    [dict(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9], profit=[20, 20, 100, 70, 60]), 150],
    [dict(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4]), 6],
])
def test_solutions(kw, expected):
    assert Solution().jobScheduling(**kw) == expected
    assert Solution1().jobScheduling(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
