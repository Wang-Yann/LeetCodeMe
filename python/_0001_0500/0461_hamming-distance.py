#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。 
# 
#  给出两个整数 x 和 y，计算它们之间的汉明距离。 
# 
#  注意： 
# 0 ≤ x, y < 231. 
# 
#  示例: 
# 
#  
# 输入: x = 1, y = 4
# 
# 输出: 2
# 
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 
# 上面的箭头指出了对应二进制位不同的位置。
#  
#  Related Topics 位运算

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hammingDistance1(self, x: int, y: int) -> int:
        ans =0
        v = x^y
        while v:
            if v&0b1:
                ans+=1
            v>>=1
        return ans

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')

        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected",[
   [dict(  x = 1, y = 4 )  ,2],
])
def test_solutions(kw,expected):
    assert Solution().hammingDistance1(**kw)==expected
    assert Solution().hammingDistance(**kw)==expected



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])




