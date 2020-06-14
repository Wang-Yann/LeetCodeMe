#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个矩阵 A， 返回 A 的转置矩阵。 
# 
#  矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#  
# 
#  示例 2： 
# 
#  输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 1000 
#  1 <= A[0].length <= 1000 
#  
#  Related Topics 数组

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        ans =[list(ele) for ele in   zip(*A)]
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)



@pytest.mark.parametrize("args,expected", [
    (
            [[1,2,3],[4,5,6],[7,8,9]]
     ,[[1,4,7],[2,5,8],[3,6,9]]),
    pytest.param([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]),
])
def test_solutions(args, expected):
    assert Solution().transpose(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

