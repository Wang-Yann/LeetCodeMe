#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 11:55:02
# @Last Modified : 2020-04-26 11:55:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#
#  注意:
#
#
#  num 的长度小于 10002 且 ≥ k。
#  num 不会包含任何前导零。
#
#
#  示例 1 :
#
#
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
#
#
#  示例 2 :
#
#
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
#
#
#  示例 3 :
#
#
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。
#
#  Related Topics 栈 贪心算法
#  👍 256 👎 0

"""
import pytest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """单调栈"""
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        # print("Raw res", stack)
        # - in the case k==0: return the entire list
        final_stack = stack[:-k] if k else stack
        return "".join(final_stack).lstrip("0") or "0"


@pytest.mark.parametrize("args,expected", [
    [("1432219", 3), "1219"],
    [("10200", 1), "200"],
    [("10", 2), "0"],

])
def test_solutions(args, expected):
    assert Solution().removeKdigits(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
