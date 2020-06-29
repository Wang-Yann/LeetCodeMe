#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个由一些 闭区间 组成的列表，每个区间列表都是成对不相交的，并且已经排序。 
# 
#  返回这两个区间列表的交集。 
# 
#  （形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b。两个闭区间的交集是一组实数，要么为空集，要么为闭区间
# 。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3]。） 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# 输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length < 1000 
#  0 <= B.length < 1000 
#  0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9 
#  
#  Related Topics 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        GOOD　TODO
        优雅
        注意利用条件　每个集合无重叠区间
        """
        ans = []
        i = j = 0
        LEN_A, LEN_B = len(A), len(B)
        while i < LEN_A and j < LEN_B:
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            if left <= right:
                ans.append([left, right])
            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
          B=[[1, 5], [8, 12], [15, 24], [25, 26]]),
     [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]],
])
def test_solutions(kw, expected):
    assert Solution().intervalIntersection(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
