#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个由 '(' 和 ')' 括号组成的字符串 S，我们需要添加最少的括号（ '(' 或是 ')'，可以在任何位置），以使得到的括号字符串有效。 
# 
#  从形式上讲，只有满足下面几点之一，括号字符串才是有效的： 
# 
#  
#  它是一个空字符串，或者 
#  它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者 
#  它可以被写作 (A)，其中 A 是有效字符串。 
#  
# 
#  给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。 
# 
#  
# 
#  示例 1： 
# 
#  输入："())"
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入："((("
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入："()"
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入："()))(("
# 输出：4 
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 1000 
#  S 只包含 '(' 和 ')' 字符。 
#  
# 
#  
#  Related Topics 栈 贪心算法

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        """
        add 左括号   需求
        balance右括号
        """
        add, balance = 0, 0
        for char in S:
            if char == "(":
                balance += 1
            else:
                balance -= 1
            if balance == -1:
                add += 1
                balance = 0
        # print(add, balance)
        return add + balance


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minAddToMakeValid(self, S: str) -> int:
        while "()" in S:
            S = S.replace("()", "")
            # 正则表达式反而慢30%
            # S=re.sub(r"(\(\))+","",S)
        return len(S)


@pytest.mark.parametrize("args,expected", [
    ("())", 1),
    ("(((", 3),
    ("()", 0),
    ("()))((", 4),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(args, expected, SolutionCLS):
    assert SolutionCLS().minAddToMakeValid(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
