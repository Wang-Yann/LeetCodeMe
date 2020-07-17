#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 13:21:04
# @Last Modified : 2020-04-25 13:21:04
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#
#  输入: "()"
# 输出: true
#
#
#  示例 2:
#
#  输入: "()[]{}"
# 输出: true
#
#
#  示例 3:
#
#  输入: "(]"
# 输出: false
#
#
#  示例 4:
#
#  输入: "([)]"
# 输出: false
#
#
#  示例 5:
#
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串
#  👍 1694 👎 0

"""

class Solution:

    def isValid(self, s: str) -> bool:
        hash_map = {"(":")", "[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in hash_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c != hash_map[last]:
                    return False
        return  len(stack)==0


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "()", "", "()[]{}", "(]", "([)]", "{[]}"
    ]
    res = [sol.isValid(args) for args in samples]
    print(res)
