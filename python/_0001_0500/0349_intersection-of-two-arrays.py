#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 14:26:38
# @Last Modified : 2020-04-30 14:26:38
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#
#  示例 1：
#
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#
#
#  示例 2：
#
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#
#
#
#  说明：
#
#
#  输出结果中的每个元素一定是唯一的。
#  我们可以不考虑输出结果的顺序。
#
#  Related Topics 排序 哈希表 双指针 二分查找
#  👍 207 👎 0

"""

from typing import List

import pytest


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
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
                if not res or res[-1] != nums1[it1]:
                    res.append(nums1[it1])
                it1 += 1
                it2 += 1

        return res


@pytest.mark.parametrize("kw,expected", [
    (dict(nums1=[1, 2, 2, 1], nums2=[2, 2]), [2]),
    (dict(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]), [9, 4]),
])
def test_solutions(kw, expected):
    res= Solution().intersection(**kw)
    assert sorted(res)==sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
