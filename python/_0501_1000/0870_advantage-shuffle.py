#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。 
# 
#  返回 A 的任意排列，使其相对于 B 的优势最大化。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
#  
# 
#  示例 2： 
# 
#  输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length = B.length <= 10000 
#  0 <= A[i] <= 10^9 
#  0 <= B[i] <= 10^9 
#  
#  Related Topics 贪心算法 数组

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA=sorted(A)
        sortedB=sorted(B)
        assigned = collections.defaultdict(list)
        remaining = []
        j=0
        for a in sortedA:
            if a>sortedB[j]:
                assigned[sortedB[j]].append(a)
                j+=1
            else:
                remaining.append(a)
        # print(assigned,remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop() for b in B]

# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A = [2,7,11,15], B = [1,10,4,11]), [2,11,7,15]),
    (dict(A = [2,0,4,1,2] , B = [1,3,0,0,2]), [2,0,2,1,4]),
    pytest.param(dict( A = [12,24,8,32], B = [13,25,32,11]  ), [24,32,8,12]),
])
def test_solutions(kwargs, expected):
    assert Solution().advantageCount(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

