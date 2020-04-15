#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 20:22:34
# @Last Modified : 2020-04-15 20:22:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List




class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """ 题意不清"""
        res =0
        end = 0
        for i,v in enumerate(timeSeries):
            if v>=end:
                end = v+duration
                res+=duration
            else:
                if i> 0:
                    delta = timeSeries[i]-timeSeries[i-1]
                    end+=delta
                    res+=delta
        return res

    def findPoisonedDurationS(self, timeSeries: List[int], duration: int) -> int:
        result = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            result -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return result






if __name__ == '__main__':
    sol = Solution()
    samples=[
        ([1,4], 2),
        ([1,2], 2),
        ([1,3,5,7,9,11,13,15],3)
    ]
    res = [ sol.findPoisonedDuration(*x) for x in samples]
    print(res)
