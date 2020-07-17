#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:16:59
# @Last Modified : 2020-04-30 15:16:59
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个非负整数的数据流输入 a1，a2，…，an，…，将到目前为止看到的数字总结为不相交的区间列表。
#
#  例如，假设数据流中的整数为 1，3，7，2，6，…，每次的总结为：
#
#  [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
#
#
#
#
#  进阶：
# 如果有很多合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
#
#  提示：
# 特别感谢 @yunhong 提供了本问题和其测试用例。
#  Related Topics 二分查找 Ordered Map
#  👍 33 👎 0

"""


from typing import List


class SummaryRanges:
    """
    TODO
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__intervals = []

    def addNum(self, val: int) -> None:
        def upper_bound(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) >> 1
                if nums[mid][0] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        i = upper_bound(self.__intervals, val)
        # print("Val|i|intervals: ",val ,i,self.__intervals)
        start, end = val, val
        if i != 0 and self.__intervals[i - 1][1] + 1 >= val:
            i -= 1
        while i != len(self.__intervals) \
                and end + 1 >= self.__intervals[i][0]:
            start = min(start, self.__intervals[i][0])
            end = max(end, self.__intervals[i][1])
            self.__intervals.pop(i)
        self.__intervals.insert(i, [start, end])

    def getIntervals(self) -> List[List[int]]:
        return self.__intervals


if __name__ == '__main__':
    obj = SummaryRanges()
    obj.addNum(1)
    obj.addNum(3)
    obj.addNum(7)
    obj.addNum(2)
    obj.addNum(3)
    obj.addNum(6)
    obj.addNum(10)
    print(obj.getIntervals())
