#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 09:54:21
# @Last Modified : 2021-02-23 09:54:21
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在 startDa
# yi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k 表示你能参加的最多会议数目。 
# 
#  你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与
# 另一个结束日期相同的两个会议。 
# 
#  请你返回能得到的会议价值 最大和 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
# 输出：7
# 解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
# 输出：10
# 解释：参加会议 2 ，得到价值和为 10 。
# 你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。 
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
# 输出：9
# 解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= events.length 
#  1 <= k * events.length <= 106 
#  1 <= startDayi <= endDayi <= 109 
#  1 <= valuei <= 106 
#  
#  Related Topics 二分查找 动态规划 
#  👍 17 👎 0

"""

import bisect
import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/discuss/1052548/Python-DP-%2B-Binary-Search
        """
        events.sort()
        starts = [x for x, y, z in events]

        @functools.lru_cache(None)
        def dp(idx, cur_k):
            if cur_k == 0 or idx >= len(events):
                return 0
            next_event = bisect.bisect_right(starts, events[idx][1])
            return max(dp(idx + 1, cur_k), events[idx][2] + dp(next_event, cur_k - 1))

        return dp(0, k)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2), 7],
    [dict(events=[[1, 2, 4], [3, 4, 3], [2, 3, 10]], k=2), 10],
    [dict(events=[[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], k=3), 9],
])
def test_solutions(kw, expected):
    assert Solution().maxValue(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
