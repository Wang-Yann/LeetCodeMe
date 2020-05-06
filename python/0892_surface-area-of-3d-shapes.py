#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1 的立方体。 
# 
#  每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。 
# 
#  请你返回最终形体的表面积。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[[2]]
# 输出：10
#  
# 
#  示例 2： 
# 
#  输入：[[1,2],[3,4]]
# 输出：34
#  
# 
#  示例 3： 
# 
#  输入：[[1,0],[0,2]]
# 输出：16
#  
# 
#  示例 4： 
# 
#  输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#  
# 
#  示例 5： 
# 
#  输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 50 
#  0 <= grid[i][j] <= 50 
#  
#  Related Topics 几何 数学

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans+=2+grid[i][j]*4
                if i:
                    ans -= min(grid[i][j],grid[i-1][j])*2
                if j:
                    ans -= min(grid[i][j],grid[i][j-1])*2
        return ans 
        
# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected",[
   ([[2]],10),
   ([[1,2],[3,4]],34),
   ([[1,0],[0,2]],16),
   ([[1,1,1],[1,0,1],[1,1,1]],32),
   ([[2,2,2],[2,1,2],[2,2,2]],46),
])
def test_solutions(args,expected):
    assert Solution().surfaceArea(args)==expected



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])




