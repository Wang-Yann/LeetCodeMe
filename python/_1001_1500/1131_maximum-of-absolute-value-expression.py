#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你两个长度相等的整数数组，返回下面表达式的最大值： 
# 
#  |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| 
# 
#  其中下标 i，j 满足 0 <= i, j < arr1.length。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# 输出：13
#  
# 
#  示例 2： 
# 
#  输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# 输出：20 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr1.length == arr2.length <= 40000 
#  -10^6 <= arr1[i], arr2[i] <= 10^6 
#  
#  Related Topics 位运算 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/solution/python-jie-fa-bao-li-shu-xue-by-jiayangwu/
        """
        A, B, C, D = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        """
            Maximum Manhattan Distance
            Take |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| as Manhattan distance of two points.
            arr1 is the coordinate of points on the x-axis,
            arr2 is the coordinate of points on the y-axis.
            For 3 points on the plane, we always have |AO| - |BO| <= |AB|.
            When AO and BO are in the same direction, we have ||AO| - |BO|| = |AB|

            We take 4 points for point O, left-top, left-bottom, right-top and right-bottom.
         """
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]
    ), 13),
    pytest.param(dict(arr1=[1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]), 20),
])
def test_solutions(kwargs, expected):
    assert Solution().maxAbsValExpr(**kwargs) == expected
    assert Solution1().maxAbsValExpr(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
