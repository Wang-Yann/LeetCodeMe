#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 21:53:49
# @Last Modified : 2020-07-22 21:53:49
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑
# 充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。 
# 
#  示例 1: 
# 
#  输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: [[7,10],[2,4]]
# 输出: 1 
#  Related Topics 堆 贪心算法 排序 
#  👍 120 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        TODO need skilled

        按照 开始时间 对会议进行排序。
            初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
            对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲。
            若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
            若房间不空闲。开新房间，并加入到堆中。
            处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。

        """
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x:x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

    def minMeetingRooms1(self, intervals):
        result, curr = 0, 0
        line = [x for i, j in intervals for x in [[i, 1], [j, -1]]]
        line.sort()
        for _, num in line:
            curr += num
            result = max(result, curr)
        return result


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 30], [5, 10], [15, 20]], 2),
    ([[7, 10], [2, 4]], 1),
])
def test_solutions253(args, expected):
    assert Solution().minMeetingRooms(args) == expected
    assert Solution().minMeetingRooms1(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
