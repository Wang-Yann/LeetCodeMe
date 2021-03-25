#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 13:14:12
# @Last Modified : 2020-05-05 13:14:12
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3]
#  米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。
#
#  编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。
#
#
#
#  示例 1:
#
#  ┌───┐
# │   │
# └───┼──>
#     │
#
# 输入: [2,1,1,2]
# 输出: true
#
#
#  示例 2:
#
#  ┌──────┐
# │      │
# │
# │
# └────────────>
#
# 输入: [1,2,3,4]
# 输出: false
#
#
#  示例 3:
#
#  ┌───┐
# │   │
# └───┼>
#
# 输入: [1,1,1,1]
# 输出: true
#
#  Related Topics 数学
#  👍 29 👎 0
from typing import List

import pytest


class Solution:

    def isSelfCrossing(self, x: List[int]) -> bool:
        """https://leetcode-cn.com/problems/self-crossing/solution/335lu-jing-jiao-cha-by-zhangll/"""
        length = len(x)
        if length >= 5 and x[3] == x[1] and x[4] + x[0] >= x[2]:
            # Crossing in a loop:
            #     2
            # 3 ┌────┐
            #   └─══>┘1
            #   4  0  (overlapped)
            return True
        for i in range(3, length):
            if x[i] >= x[i - 2] and x[i - 3] >= x[i - 1]:
                # Case 1:
                #    i-2
                # i-1┌─┐
                #    └─┼─>i
                #     i-3
                return True
            elif i >= 5 \
                    and x[i - 4] <= x[i - 2] <= x[i] + x[i - 4] \
                    and x[i - 1] <= x[i - 3] <= x[i - 5] + x[i - 1]:
                # Case 2:
                #    i-4
                #    ┌──┐
                #    │i<┼─┐
                # i-3│ i-5│i-1
                #    └────┘
                #      i-2
                return True
        return False

class Solution1:
    def isSelfCrossing(self, x) -> bool:
        if len(x) <  4:return False
        if len(x) == 4:return   x[3] >= x[1] and x[2] <= x[0]
        for i in range(3, len(x)):
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True
            if i > 3 and x[i-1] == x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True
            if i > 4 and x[i-3]-x[i-5] <= x[i-1] <= x[i-3] and x[i-2]-x[i-4] <= x[i] <= x[i-2] and x[i-2] > x[i-4]:
                return True
        return False



@pytest.mark.parametrize("args,expected", [
    ([2, 1, 1, 2], True),
    ([1, 1, 1, 1], True),
    pytest.param([1, 2, 3, 4], False),
])
def test_solutions(args, expected):
    assert Solution().isSelfCrossing(args) == expected
    assert Solution1().isSelfCrossing(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
