#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。 
# 
#  你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返
# 回当前数据流中第K大的元素。 
# 
#  示例: 
# 
#  
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3); // returns 4
# kthLargest.add(5); // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9); // returns 8
# kthLargest.add(4); // returns 8
#  
# 
#  说明: 
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。 
#  Related Topics 堆

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.__k = k
        self.__min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.__min_heap, val)
        if len(self.__min_heap) > self.__k:
            heapq.heappop(self.__min_heap)
        return self.__min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    k = 3
    arr = [4, 5, 8, 2]
    obj = KthLargest(k, arr)
    assert obj.add(3) == 4  # returns 4
    assert obj.add(5) == 5  # returns 5
    assert obj.add(10) == 5  # returns 5
    assert obj.add(9) == 8  # returns 8
    assert obj.add(4) == 8  # returns 8


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
