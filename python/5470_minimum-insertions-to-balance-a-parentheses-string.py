#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 02:08:29
# @Last Modified : 2020-08-09 02:08:29
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足： 
# 
#  
#  任何左括号 '(' 必须对应两个连续的右括号 '))' 。 
#  左括号 '(' 必须在对应的连续两个右括号 '))' 之前。 
#  
# 
#  比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。 
# 
#  你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。 
# 
#  请你返回让 s 平衡的最少插入次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "(()))"
# 输出：1
# 解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串 "(())))"
#  。
#  
# 
#  示例 2： 
# 
#  输入：s = "())"
# 输出：0
# 解释：字符串已经平衡了。
#  
# 
#  示例 3： 
# 
#  输入：s = "))())("
# 输出：3
# 解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
#  
# 
#  示例 4： 
# 
#  输入：s = "(((((("
# 输出：12
# 解释：添加 12 个 ')' 得到平衡字符串。
#  
# 
#  示例 5： 
# 
#  输入：s = ")))))))"
# 输出：5
# 解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 只包含 '(' 和 ')' 。 
#  
#  Related Topics 栈 字符串 
#  👍 0 👎 0
	 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minInsertions(self, s: str) -> int:
        """我的第一思路也是这样，没写出来"""
        s = s.replace('))', '*')
        ans = s.count(')')
        s = s.replace(')', '*')
        while "(*" in s:
            s = s.replace('(*', '')
        # print(s)
        return ans + len(s) + s.count('(')


# leetcode submit region end(Prohibit modification and deletion)


class Solution5470:

    def minInsertions(self, s: str) -> int:
        """AC 也是完了才做出来"""
        ans = 0
        stack = []
        i = 0
        N = len(s)
        while i < N:
            char = s[i]
            if char == "(":
                stack.append("(")
                i += 1
                continue
            if i < N - 1 and s[i + 1] == ")":
                if not stack:
                    ans += 1
                else:
                    stack.pop()
                i += 2
            else:
                if stack:
                    ans += 1
                    stack.pop()
                else:
                    ans += 2
                i += 1
        if stack:
            ans += 2 * len(stack)
        return ans


class Solution2:

    def minInsertions(self, s: str) -> int:
        """
            need 记录需右括号的需求量
            res 左括号

        """
        res = need = 0
        for char in s:
            if char == "(":
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            elif char == ")":
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="(()))"), 1],
    pytest.param(dict(s="())"), 0),
    pytest.param(dict(s="))())("), 3),
    pytest.param(dict(s="(((((("), 12),
    pytest.param(dict(s=")))))))"), 5),
    pytest.param(dict(s="(()))(()))()())))"), 4),
    pytest.param(dict(s="((())))))"), 0),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution5470, Solution2])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().minInsertions(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
