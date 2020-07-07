#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 e
# ndDayi 。 
# 
#  你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。 
# 
#  请你返回你可以参加的 最大 会议数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
#  
# 
#  示例 2： 
# 
#  输入：events= [[1,2],[2,3],[3,4],[1,2]]
# 输出：4
#  
# 
#  示例 3： 
# 
#  输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# 输出：4
#  
# 
#  示例 4： 
# 
#  输入：events = [[1,100000]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# 输出：7
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= events.length <= 10^5 
#  events[i].length == 2 
#  1 <= events[i][0] <= events[i][1] <= 10^5 
#  
#  Related Topics 贪心算法 排序 线段树

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        GOOD GOOD GOOD TODO
        扫描线＋贪心
        注意
        # 因为 endDay  大的会议可选择的空间是比 endDay  小的多的，所以在满足条件的会议需要让 endDay 小的先开。
        Iterate from the day 1 to day 100000,
        Each day, we add new events starting on day d to the queue pq.
        Also we remove the events that are already closed.

        Then we greedily attend the event that ends soonest.
        If we can attend a meeting, we increment the result res.

        """
        events.sort(reverse=True)
        min_heap = []
        res = d = 0
        while events or min_heap:
            if not min_heap:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                ele = events.pop()
                heapq.heappush(min_heap, ele[1])
            heapq.heappop(min_heap)
            res += 1
            d += 1
            while min_heap and min_heap[0] < d:
                heapq.heappop(min_heap)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(events=[[1, 2], [2, 3], [3, 4]]), 3],
    [dict(events=[[1, 2], [2, 3], [3, 4], [1, 2]]), 4],
    [dict(events=[[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]), 4],
    [dict(events=[[1, 100000]]), 1],
    [dict(events=[[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]]), 7],
])
def test_solutions(kw, expected):
    assert Solution().maxEvents(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
