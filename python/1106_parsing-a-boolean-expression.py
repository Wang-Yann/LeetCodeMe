#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。 
# 
#  有效的表达式需遵循以下约定： 
# 
#  
#  "t"，运算结果为 True 
#  "f"，运算结果为 False 
#  "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT） 
#  "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND） 
#  "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR） 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：expression = "!(f)"
# 输出：true
#  
# 
#  示例 2： 
# 
#  输入：expression = "|(f,t)"
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：expression = "&(t,f)"
# 输出：false
#  
# 
#  示例 4： 
# 
#  输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 20000 
#  expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。 
#  expression 是以上述形式给出的有效表达式，表示一个布尔值。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ')':
                seen = set()
                while stack[-1] != '(':
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(all(seen) if operator == '&' else any(seen) if operator == '|' else not seen.pop())
            elif c != ',':
                stack.append(True if c == 't' else False if c == 'f' else c)
        return stack.pop()


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def parseBoolExpr(self, expression: str) -> bool:
        t = True
        f = False
        return eval(expression.replace('!', 'not |').replace('&(', 'all([').replace('|(', 'any([').replace(')', '])'))


@pytest.mark.parametrize("kw,expected", [
    [dict(expression="!(f)"), True],
    [dict(expression="|(f,t)"), True],
    [dict(expression="&(t,f)"), False],
    [dict(expression="|(&(t,f,t),!(t))"), False],
])
def test_solutions(kw, expected):
    assert Solution().parseBoolExpr(**kw) == expected
    assert Solution1().parseBoolExpr(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
