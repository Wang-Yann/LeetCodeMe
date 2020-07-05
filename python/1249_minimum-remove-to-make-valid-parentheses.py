#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 14:41:26
# @Last Modified : 2020-07-05 14:41:26
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个由 '('、')' 和小写字母组成的字符串 s。 
# 
#  你需要从字符串中删除最少数目的 '(' 或者 ')' （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。 
# 
#  请返回任意一个合法字符串。 
# 
#  有效「括号字符串」应当符合以下 任意一条 要求： 
# 
#  
#  空字符串或只包含小写字母的字符串 
#  可以被写作 AB（A 连接 B）的字符串，其中 A 和 B 都是有效「括号字符串」 
#  可以被写作 (A) 的字符串，其中 A 是一个有效的「括号字符串」 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "lee(t(c)o)de)"
# 输出："lee(t(c)o)de"
# 解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。
#  
# 
#  示例 2： 
# 
#  输入：s = "a)b(c)d"
# 输出："ab(c)d"
#  
# 
#  示例 3： 
# 
#  输入：s = "))(("
# 输出：""
# 解释：空字符串也是有效的
#  
# 
#  示例 4： 
# 
#  输入：s = "(a(b(c)d)"
# 输出："a(b(c)d)"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s[i] 可能是 '('、')' 或英文小写字母 
#  
#  Related Topics 栈 字符串 
#  👍 38 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        lst = list(s)
        stack = []
        for i, char in enumerate(lst):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    lst[i] = ""
        # print(stack)
        for i in stack:
            lst[i] = ""
        return "".join(lst)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="lee(t(c)o)de)"), ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]),
    pytest.param(dict(s="a)b(c)d"), ["ab(c)d"]),
    pytest.param(dict(s="))(("), [""]),
    pytest.param(dict(s="(a(b(c)d)"), ["a(b(c)d)"]),
])
def test_solutions(kwargs, expected):
    assert Solution().minRemoveToMakeValid(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
