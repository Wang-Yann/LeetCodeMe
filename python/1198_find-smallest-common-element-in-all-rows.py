#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 16:22:04
# @Last Modified : 2020-08-05 16:22:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个矩阵 mat，其中每一行的元素都已经按 递增 顺序排好了。请你帮忙找出在所有这些行中 最小的公共元素。 
# 
#  如果矩阵中没有这样的公共元素，就请返回 -1。 
# 
#  
# 
#  示例： 
# 
#  输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= mat.length, mat[i].length <= 500 
#  1 <= mat[i][j] <= 10^4 
#  mat[i] 已按递增顺序排列。 
#  
#  Related Topics 哈希表 二分查找 
#  👍 9 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        lookup = collections.Counter()
        N = len(mat)
        for row in mat:
            for v in row:
                lookup[v] += 1
        for num in sorted(lookup):
            if lookup[num] == N:
                return num
        return -1


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def smallestCommonElement(self, mat):
        # values could be duplicated in each row
        intersections = set(mat[0])
        for i in range(1, len(mat)):
            intersections &= set(mat[i])
            if not intersections:
                return -1
        return min(intersections)


@pytest.mark.parametrize("kw,expected", [
    [dict(mat=[[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]), 5],
])
def test_solutions(kw, expected):
    assert Solution().smallestCommonElement(**kw) == expected
    assert Solution1().smallestCommonElement(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
