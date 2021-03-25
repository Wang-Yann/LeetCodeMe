#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 22:36:16
# @Last Modified : 2020-05-05 22:36:16
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
#
#  如果没有两个连续的 1，返回 0 。
#
#
#
#
#
#
#  示例 1：
#
#  输入：22
# 输出：2
# 解释：
# 22 的二进制是 0b10110 。
# 在 22 的二进制表示中，有三个 1，组成两对连续的 1 。
# 第一对连续的 1 中，两个 1 之间的距离为 2 。
# 第二对连续的 1 中，两个 1 之间的距离为 1 。
# 答案取两个距离之中最大的，也就是 2 。
#
#
#  示例 2：
#
#  输入：5
# 输出：2
# 解释：
# 5 的二进制是 0b101 。
#
#
#  示例 3：
#
#  输入：6
# 输出：1
# 解释：
# 6 的二进制是 0b110 。
#
#
#  示例 4：
#
#  输入：8
# 输出：0
# 解释：
# 8 的二进制是 0b1000 。
# 在 8 的二进制表示中没有连续的 1，所以返回 0 。
#
#
#
#
#  提示：
#
#
#  1 <= N <= 10^9
#
#  Related Topics 数学
#  👍 51 👎 0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

class Solution:
    def binaryGap(self, N: int) -> int:
        ans = 0
        i=0
        #32位 int
        pre=32
        while N:
            if N&0b1==1:
                ans = max(ans,i-pre)
                pre=i
            i+=1
            N>>=1
        return ans





@pytest.mark.parametrize("args,expected", [
    (22, 2),
    (5, 2),
    (6, 1),
    (8, 0),
])
def test_solutions(args, expected):
    assert Solution().binaryGap(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


