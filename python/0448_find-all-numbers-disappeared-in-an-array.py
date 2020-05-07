#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。 
# 
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
# 
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
# 
#  示例: 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
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
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        遍历输入数组的每个元素一次。
        我们将把 |nums[i]|-1 索引位置的元素标记为负数。即 nums[|nums[i] |- 1] *(-1) 。
        然后遍历数组，若当前数组元素 nums[i] 为负数，说明我们在数组中存在数字 i+1。
        """
        for i in range(len(nums)):
            new_index=abs(nums[i])-1
            if nums[new_index]>0:
                nums[new_index]*=-1
        res = []
        for i in range(1,len(nums)+1):
            if nums[i-1]>0:
                res.append(i)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    O(N)不符合要求
    """
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums)+1))-set(nums))

@pytest.mark.parametrize("args,expected",[
   ( [4,3,2,7,8,2,3,1],[5,6])
])
def test_solutions(args,expected):
    assert sorted(Solution().findDisappearedNumbers(args))==sorted(expected)



if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])




