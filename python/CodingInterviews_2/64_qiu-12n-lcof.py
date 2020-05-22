#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。 
# 
#  
# 
#  示例 1： 
# 
#  输入: n = 3
# 输出: 6
#  
# 
#  示例 2： 
# 
#  输入: n = 9
# 输出: 45
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 10000 
#  
# 

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(1,n+1))

# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def sumNums(self, n: int) -> int:
        if n==1:
            return 1
        n+=self.sumNums(n-1 )
        return n

@pytest.mark.parametrize("args,expected", [
    (3, 6),
    pytest.param(9,45),
])
def test_solutions(args, expected):
    assert Solution().sumNums(args) == expected
    assert Solution1().sumNums(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])