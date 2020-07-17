#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-29 16:52:51
# @Last Modified : 2020-04-29 16:52:51
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照升序排列。编写一个方法，计算出研究者的 h 指数。
#
#  h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别
# 被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"
#
#
#
#  示例:
#
#  输入: citations = [0,1,3,5,6]
# 输出: 3
# 解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
#      由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。
#
#
#
#  说明:
#
#  如果 h 有多有种可能的值 ，h 指数是其中最大的那个。
#
#
#
#  进阶：
#
#
#  这是 H指数 的延伸题目，本题中的 citations 数组是保证有序的。
#  你可以优化你的算法到对数时间复杂度吗？
#
#  Related Topics 二分查找
#  👍 57 👎 0

"""

from typing import List

import pytest


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        length = len(citations)
        l, r = 0, length - 1
        #查找第一个value >=length-i 时　的l
        while l <= r:
            mid = (l + r) // 2
            if citations[mid] > length - mid:
                r -= 1
            elif citations[mid] < length - mid:
                l += 1
            else:
                return length-mid
        return length - l


@pytest.mark.parametrize("args,expected", [
    ([0, 1, 3, 5, 6], 3),
    ([], 0),
    ([0], 0),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.hIndex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
