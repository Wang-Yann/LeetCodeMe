#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。 
# 
#  定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。 
# 
#  找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。 
# 
#  示例 1: 
# 
#  输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#      [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#  
# 
#  示例 2: 
# 
#  输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#  
# 
#  示例 3: 
# 
#  输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
#  
#  Related Topics 堆

"""
import heapq
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for x in nums1:
            for y in nums2:
                sum_val = x + y
                heapq.heappush(heap, (-sum_val, x, y))
                if len(heap) > k:
                    heapq.heappop(heap)
        return [[x, y] for _, x, y in heapq.nsmallest(k, heap)[::-1]]

    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return [list(x) for x in heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum)]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3), [[1, 2], [1, 4], [1, 6]]),
    pytest.param(dict(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2), [[1, 1], [1, 1]]),
    pytest.param(dict(nums1=[1, 2], nums2=[3], k=3), [[1, 3], [2, 3]]),
])
def test_solutions(kwargs, expected):
    assert Solution().kSmallestPairs(**kwargs) == expected
    assert Solution().kSmallestPairs1(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
