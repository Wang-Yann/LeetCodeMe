#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 20:48:26
# @Last Modified : 2020-04-11 20:48:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        res = []
        for i in range(0,len(intervals)):
            v = intervals[i]
            if i>0 and v[0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1],v[1])
            else:
                res.append(v)
        return res





if __name__ == '__main__':
    sol = Solution()
    sample = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]]
    ]
    print([sol.merge(x) for x in sample])
