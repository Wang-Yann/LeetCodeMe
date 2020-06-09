#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则： 
# 
#  
#  任何左括号 ( 必须有相应的右括号 )。 
#  任何右括号 ) 必须有相应的左括号 ( 。 
#  左括号 ( 必须在对应的右括号之前 )。 
#  * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。 
#  一个空字符串也被视为有效字符串。 
#  
# 
#  示例 1: 
# 
#  
# 输入: "()"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "(*)"
# 输出: True
#  
# 
#  示例 3: 
# 
#  
# 输入: "(*))"
# 输出: True
#  
# 
#  注意: 
# 
#  
#  字符串大小将在 [1，100] 范围内。 
#  
#  Related Topics 字符串

"""
import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        贪心
        在处理字符串中的当前字符时，让 lo、hi 分别为可能的最小和最大左括号数。
        如果我们遇到左括号（c == '('），那么 lo++，若遇到右括号，则 lo--。
        如果我们遇到 * 号且可以转换成左括号（c != ')'），则 hi++，否则我们转换成右括号，所以 hi--。
        如果 hi<0 ，那么无论我们选择什么，当前情况都无法生成有效的括号。而且，左括号不能小于0。
        最后，我们应该检查一下是否可以有 0 个左括号。

        """
        # keep lower bound and upper bound of '(' counts
        lower, upper = 0, 0
        for char in s:
            if char == "(":
                lower += 1
                upper += 1
            elif char == ")":
                upper -= 1
                lower -= 1
            else:
                lower -= 1
                upper += 1
            if upper < 0:
                break
            lower = max(lower, 0)
        # range of '(' count is valid
        return lower == 0


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def checkValidString(self, s: str) -> bool:
        length = len(s)
        if not length:
            return True

        @functools.lru_cache(None)
        def helper(idx, stack):
            if stack < 0:
                return False
            if idx == length:
                return stack == 0
            char = s[idx]
            if char == "(":
                return helper(idx + 1, stack + 1)
            elif char == ")":
                return helper(idx + 1, stack - 1)
            else:
                return helper(idx + 1, stack + 1) or helper(idx + 1, stack - 1) or helper(idx + 1, stack)

        return helper(0, 0)


@pytest.mark.parametrize("args,expected", [
    ("()", True),
    ("(*)", True),
    ("(*))", True),
    ("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())", False),
])
def test_solutions(args, expected):
    assert Solution().checkValidString(args) == expected
    assert Solution1().checkValidString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
