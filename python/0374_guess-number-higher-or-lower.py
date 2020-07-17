#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 15:46:09
# @Last Modified : 2020-04-30 15:46:09
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
#
#  -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
#
#
#
#
#  示例 :
#
#  输入: n = 10, pick = 6
# 输出: 6
#  Related Topics 二分查找
#  👍 66 👎 0

"""

import pytest

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
TARGET = 6


def guess(num: int) -> int:
    if num < TARGET:
        return 1
    elif num > TARGET:
        return -1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) >> 1
            if guess(mid) == 1:
                l = mid + 1
            elif guess(mid) == -1:
                r = mid - 1
            else:
                return mid
        return l


@pytest.mark.parametrize("args,expected", [
    (10, 6)
])
def test_solutions(args, expected):
    assert Solution().guessNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
