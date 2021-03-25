#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这里有 n 门不同的在线课程，他们按从 1 到 n 编号。每一门课程有一定的持续上课时间（课程时间）t 以及关闭时间第 d 天。一门课要持续学习 t 天直到
# 第 d 天时要完成，你将会从第 1 天开始。 
# 
#  给出 n 个在线课程用 (t, d) 对表示。你的任务是找出最多可以修几门课。 
# 
#  
# 
#  示例： 
# 
#  
# 输入: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# 输出: 3
# 解释: 
# 这里一共有 4 门课程, 但是你最多可以修 3 门:
# 首先, 修第一门课时, 它要耗费 100 天，你会在第 100 天完成, 在第 101 天准备下门课。
# 第二, 修第三门课时, 它会耗费 1000 天，所以你将在第 1100 天的时候完成它, 以及在第 1101 天开始准备下门课程。
# 第三, 修第二门课时, 它会耗时 200 天，所以你将会在第 1300 天时完成它。
# 第四门课现在不能修，因为你将会在第 3300 天完成它，这已经超出了关闭日期。 
# 
#  
# 
#  提示: 
# 
#  
#  整数 1 <= d, t, n <= 10,000 。 
#  你不能同时修两门课程。 
#  
# 
#  
#  Related Topics 贪心算法

"""
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        从左到右扫描每个课程，依次学习。如果发现学了之后超过 deadline 的，就从之前学过的课程里扔掉一个耗时最长的。
         因为这样可以使得其他的课程往前挪，而往前挪是没影响的.
         GOOD
        """
        courses.sort(key=lambda x: x[1])
        now = 0
        max_heap = []
        for period, deadline in courses:
            now = now + period
            heapq.heappush(max_heap, -period)
            if now > deadline:
                now += heapq.heappop(max_heap)
        return len(max_heap)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
    ([[1, 2], [2, 3]], 2),
    ([[5, 5], [4, 6], [2, 6]], 2)
])
def test_solutions(args, expected):
    assert Solution().scheduleCourse(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
