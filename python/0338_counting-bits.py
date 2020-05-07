#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,1] 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: [0,1,1,2,1,2] 
# 
#  进阶: 
# 
#  
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？ 
#  要求算法的空间复杂度为O(n)。 
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。 
#  
#  Related Topics 位运算 动态规划

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    DP
    P(x)=P(x&(x-1))+1
    使用最后设置位。 最后设置位是从右到左第一个为1的位。使用 x &= x - 1 将该位设置为0

    """
    def countBits(self, num: int) -> List[int]:
        dp=[0]*(num+1)
        for i in range(1,num+1):
            dp[i]=dp[i&(i-1)]+1
        return dp


        
# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    DP
    P(x)=P(x/2)+(x mod 2)
    x/2 ==> x>>1
    x mod 2 ==> x & 1
    """
    def countBits(self, num: int) -> List[int]:
        res=[0]
        for i in range(1,num+1):
            res.append((i&0b1) + res[i>>1])
        return  res



@pytest.mark.parametrize("args,expected",[
   (0, [0] ),
   (2, [0,1,1] ),
   (5,[0,1,1,2,1,2]) ,
   (17,[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2])
])
def test_solutions(args,expected):
    assert Solution().countBits(args)==expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])




