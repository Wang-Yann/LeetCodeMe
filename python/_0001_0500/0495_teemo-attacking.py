#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-15 20:22:34
# @Last Modified : 2020-04-15 20:22:34
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击
# 的中毒持续时间，你需要输出艾希的中毒状态总时长。
#
#  你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。
#
#
#
#  示例1:
#
#  输入: [1,4], 2
# 输出: 4
# 原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
# 第 4 秒初，提莫再次攻击艾希，使得艾希获得另外 2 秒中毒时间。
# 所以最终输出 4 秒。
#
#
#  示例2:
#
#  输入: [1,2], 2
# 输出: 3
# 原因: 第 1 秒初，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持 2 秒钟，直到第 2 秒末结束。
# 但是第 2 秒初，提莫再次攻击了已经处于中毒状态的艾希。
# 由于中毒状态不可叠加，提莫在第 2 秒初的这次攻击会在第 3 秒末结束。
# 所以最终输出 3 。
#
#
#
#
#  提示：
#
#
#  你可以假定时间序列数组的总长度不超过 10000。
#  你可以假定提莫攻击时间序列中的数字和提莫攻击的中毒持续时间都是非负整数，并且不超过 10,000,000。
#
#  Related Topics 数组
#  👍 90 👎 0

"""

from typing import List

import pytest


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """ 题意不清"""
        res = 0
        end = 0
        for i, v in enumerate(timeSeries):
            if v >= end:
                end = v + duration
                res += duration
            else:
                if i > 0:
                    delta = timeSeries[i] - timeSeries[i - 1]
                    end += delta
                    res += delta
        return res


class Solution1:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = duration * len(timeSeries)
        for i in range(1, len(timeSeries)):
            result -= max(0, duration - (timeSeries[i] - timeSeries[i - 1]))
        return result


@pytest.mark.parametrize("args,expected", [
    (([1, 4], 2), 4),
    (([1, 2], 2), 3),
    (([1, 3, 5, 7, 9, 11, 13, 15], 3), 17),
])
def test_solutions(args, expected):
    assert Solution().findPoisonedDuration(*args) == expected
    assert Solution1().findPoisonedDuration(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
