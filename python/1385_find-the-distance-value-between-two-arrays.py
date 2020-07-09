#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。 
# 
#  「距离值」 定义为符合此描述的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# 输出：2
# 解释：
# 对于 arr1[0]=4 我们有：
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# 对于 arr1[1]=5 我们有：
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# 对于 arr1[2]=8 我们有：
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
#  
# 
#  示例 2： 
# 
#  
# 输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= arr1.length, arr2.length <= 500 
#  -10^3 <= arr1[i], arr2[j] <= 10^3 
#  0 <= d <= 100 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        counter = collections.Counter(arr2)
        ans = 0
        for v in arr1:
            if any(counter[x] for x in range(v - d, v + d + 1)):
                continue
            ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2), 2],
    [dict(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3), 2],
    [dict(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6), 1],
])
def test_solutions(kw, expected):
    assert Solution().findTheDistanceValue(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
