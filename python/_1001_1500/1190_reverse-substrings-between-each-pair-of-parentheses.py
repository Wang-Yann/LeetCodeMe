#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个字符串 s（仅含有小写英文字母和括号）。 
# 
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。 
# 
#  注意，您的结果中 不应 包含任何括号。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "(abcd)"
# 输出："dcba"
#  
# 
#  示例 2： 
# 
#  输入：s = "(u(love)i)"
# 输出："iloveu"
#  
# 
#  示例 3： 
# 
#  输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#  
# 
#  示例 4： 
# 
#  输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 2000 
#  s 中只有小写英文字母和括号 
#  我们确保所有括号都是成对出现的 
#  
#  Related Topics 栈

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        """GOOD"""
        stack = [[]]
        for char in s:
            if char == "(":
                stack.append([])
            elif char == ")":
                end = stack.pop()
                end.reverse()
                stack[-1].extend(end)
            else:
                stack[-1].append(char)
        # print(stack)
        return "".join(stack.pop())


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(s="(abcd)"), "dcba"],
    [dict(s="(u(love)i)"), "iloveu"],
    [dict(s="(ed(et(oc))el)"), "leetcode"],
    [dict(s="a(bcdefghijkl(mno)p)q"), "apmnolkjihgfedcbq"],
])
def test_solutions(kw, expected):
    assert Solution().reverseParentheses(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
