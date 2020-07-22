#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 15:00:24
# @Last Modified : 2020-04-27 15:00:24
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# search-in-rotated-sorted-array
import heapq
import math
from typing import List

import pytest


# 251
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.data = []
        for l in v:
            self.data.extend(l)
        self.pos = -1

    def next(self) -> int:
        self.pos += 1
        return self.data[self.pos]

    def hasNext(self) -> bool:
        return self.pos < len(self.data) - 1


def test_solution251():
    iterator = Vector2D([[1, 2], [3], [4]])

    assert iterator.next() == 1
    assert iterator.next() == 2
    assert iterator.next() == 3
    assert iterator.hasNext()
    assert iterator.hasNext()
    assert iterator.next() == 4
    assert not iterator.hasNext()


class Solution252:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))


@pytest.mark.parametrize("args,expected", [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
])
def test_solutions252(args, expected):
    assert Solution252().canAttendMeetings(args) == expected


class Solution253:
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
        intervals.sort(key=lambda x: x[0])

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


@pytest.mark.parametrize("args,expected", [
    ([[0, 30], [5, 10], [15, 20]], 2),
    ([[7, 10], [2, 4]], 1),
])
def test_solutions253(args, expected):
    assert Solution253().minMeetingRooms(args) == expected
    assert Solution253().minMeetingRooms1(args) == expected


class Solution254:
    def getFactors(self, n: int) -> List[List[int]]:
        """GOOD"""
        res = []

        def dfs(num, factors):
            i = 2 if not factors else factors[-1]
            while i <= num // i:
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
                    res.append(list(factors))
                    factors.pop()
                    dfs(num // i, factors)
                    factors.pop()
                i += 1

        dfs(n, [])
        return res


@pytest.mark.parametrize("args,expected", [
    (1, []),
    (37, []),
    (12, [
        [2, 6],
        [2, 2, 3],
        [3, 4]
    ]),
    (32, [
        [2, 16],
        [2, 2, 8],
        [2, 2, 2, 4],
        [2, 2, 2, 2, 2],
        [2, 4, 4],
        [4, 8]
    ]
     ),
])
def test_solutions(args, expected):
    assert sorted(Solution254().getFactors(args)) == sorted(expected)


#


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
