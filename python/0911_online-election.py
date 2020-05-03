#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 15:01:48
# @Last Modified : 2020-05-03 15:01:48
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import bisect
import collections
from typing import List


class TopVotedCandidate:
    """每当选票记录，我们可以记录每个胜者改变的 (winner, time) 时刻信息。之后，我们拥有一个有序的时刻信息，并用二分搜索找到答案。"""

    def __init__(self, persons: List[int], times: List[int]):
        self.A = []
        count = collections.Counter()
        # leader, num votes for leader
        leader, num = None, 0
        for p, t in zip(persons, times):
            count[p] += 1
            cur_num = count[p]
            if cur_num >= num:
                if p != leader:
                    leader = p
                    self.A.append((t, leader))
                if cur_num > num:
                    num = cur_num

    def q(self, t: int) -> int:
        idx = bisect.bisect_left(self.A, (t, float("inf")), 1)
        return self.A[idx - 1][1]


if __name__ == '__main__':
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    ops_list = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    args_list = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]

    # output [null,0,1,1,0,0,1]
    for i in range(1, len(ops_list)):
        method, args = ops_list[i], args_list[i]
        print(getattr(obj, method)(*args))
