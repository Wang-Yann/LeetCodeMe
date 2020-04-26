#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 14:22:38
# @Last Modified : 2020-04-26 14:22:38
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """单调栈"""
        stack = []
        monotonic_dic={}
        for num in nums2:
            while stack and num>stack[-1]:
                monotonic_dic[stack.pop()]=num
            stack.append(num)
        while stack:
            monotonic_dic[stack.pop()]=-1
        return [monotonic_dic[x] for x in nums1]
        


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([4, 1, 2], [1, 3, 4, 2]),
        ([2, 4], [1, 2, 3, 4]),

    ]
    lists = [x for x in samples]
    res = [sol.nextGreaterElement(*x) for x in lists]
    print(res)
