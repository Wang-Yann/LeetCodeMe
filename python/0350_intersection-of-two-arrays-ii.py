#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 14:26:38
# @Last Modified : 2020-04-30 14:26:38
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from typing import List

import pytest


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []
        it1, it2 = 0, 0
        while it1 <= len(nums1) - 1 and it2 <= len(nums2) - 1:
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res.append(nums1[it1])
                it1 += 1
                it2 += 1

        return res
    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums1) & collections.Counter(nums2)
        ans = []
        for i in c:
            ans.extend([i]*c[i])
        return ans


@pytest.mark.parametrize("kw,expected", [
    (dict(nums1=[1,2,2,2,1], nums2=[2, 2]), [2,2]),
    # (dict(nums1=[4, 9, 5], nums2=[9,4,9,8,4]), [9, 4]),
])
def test_solutions(kw, expected):
    # res= Solution().intersect(**kw)
    res= Solution().intersect2(**kw)
    assert sorted(res)==sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
    
