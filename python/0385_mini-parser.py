#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:34:59
# @Last Modified : 2020-04-26 10:34:59
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
#
#  列表中的每个元素只可能是整数或整数嵌套列表
#
#  提示：你可以假定这些字符串都是格式良好的：
#
#
#  字符串非空
#  字符串不包含空格
#  字符串只包含数字0-9、[、-、,、]
#
#
#
#
#  示例 1：
#
#  给定 s = "324",
#
# 你应该返回一个 NestedInteger 对象，其中只包含整数值 324。
#
#
#  示例 2：
#
#  给定 s = "[123,[456,[789]]]",
#
# 返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
#
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
#     i.  一个 integer 包含值 456
#     ii. 一个包含一个元素的嵌套列表
#          a. 一个 integer 包含值 789
#
#  Related Topics 栈 字符串
#  👍 38 👎 0

"""

from common_utils import NestedInteger


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        """TODO"""
        if not s:
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        # 查找数字
        i = 0
        for j in range(len(s)):
            if s[j] == "[":
                stack += [NestedInteger()]
                i = j + 1
            elif s[j] in ",]":
                if s[j - 1].isdigit():
                    stack[-1].add(NestedInteger(int(s[i:j])))
                # 此时为嵌套列表
                if s[j] == "]" and len(stack) > 1:
                    cur = stack.pop()
                    stack[-1].add(cur)
                i = j + 1

        return stack[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.deserialize("[1]"))
