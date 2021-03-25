#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。 
# 
#  因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。） 
# 
#  返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。 
# 
#  如果有多个答案，你可以返回其中任何一个。保证答案存在。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [1,1], B = [2,2]
# 输出：[1,2]
#  
# 
#  示例 2： 
# 
#  输入：A = [1,2], B = [2,3]
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  输入：A = [2], B = [1,3]
# 输出：[2,3]
#  
# 
#  示例 4： 
# 
#  输入：A = [1,2,5], B = [2,4]
# 输出：[5,4]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= B.length <= 10000 
#  1 <= A[i] <= 100000 
#  1 <= B[i] <= 100000 
#  保证爱丽丝与鲍勃的糖果总量不同。 
#  答案肯定存在。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        delta = (sum(A) - sum(B)) // 2
        setB = set(B)
        for v in set(A):
            if v - delta in setB:
                return [v, v - delta]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[1, 1], B=[2, 2]), [1, 2]),
    pytest.param(dict(A=[1, 2], B=[2, 3]), [1, 2]),
    pytest.param(dict(A=[2], B=[1, 3]), [2, 3]),
    pytest.param(dict(A=[1, 2, 5], B=[2, 4]), [5, 4]),
])
def test_solutions(kwargs, expected):
    assert Solution().fairCandySwap(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
