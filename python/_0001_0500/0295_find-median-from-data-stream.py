#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例： 
# 
#  addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2 
# 
#  进阶: 
# 
#  
#  如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？ 
#  如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？ 
#  
#  Related Topics 堆 设计

"""
import heapq
import pytest

# leetcode submit region begin(Prohibit modification and deletion)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__min_heap = []
        self.__max_heap = []

    def addNum(self, num: int) -> None:
        if not self.__max_heap or num > -self.__max_heap[0]:
            heapq.heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heapq.heappush(self.__max_heap, -heapq.heappop(self.__min_heap))
        else:
            heapq.heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap):
                heapq.heappush(self.__min_heap, -heapq.heappop(self.__max_heap))

    def findMedian(self) -> float:
        if len(self.__max_heap) == len(self.__min_heap):
            return (-self.__max_heap[0] + self.__min_heap[0]) / 2.0
        else:
            return self.__min_heap[0]

    def __str__(self) -> str:
        return "min_heap:{} \n max_heap:{}".format(self.__min_heap,self.__max_heap)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(22)
    obj.addNum(20)
    obj.addNum(10)
    obj.addNum(9)
    obj.addNum(7)
    obj.addNum(28)
    obj.addNum(29)
    obj.addNum(30)
    obj.addNum(5)
    obj.addNum(6)
    param_2 = obj.findMedian()
    assert param_2 == 10


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
