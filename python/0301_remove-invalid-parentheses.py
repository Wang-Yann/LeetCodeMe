#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。 
# 
#  说明: 输入可能包含了除 ( 和 ) 以外的字符。 
# 
#  示例 1: 
# 
#  输入: "()())()"
# 输出: ["()()()", "(())()"]
#  
# 
#  示例 2: 
# 
#  输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
#  
# 
#  示例 3: 
# 
#  输入: ")("
# 输出: [""] 
#  Related Topics 深度优先搜索 广度优先搜索

"""

from typing import List

import pytest


# https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/bfsjian-dan-er-you-xiang-xi-de-pythonjiang-jie-by-/
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            """Isvalid Parentheses"""
            cnt = 0
            for c in s:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        level = {s}
        while True:
            valid_res = list(filter(isValid, level))
            if valid_res:
                return valid_res
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":
                        # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i] + item[i + 1:])
            level = next_level


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("()())()", ["()()()", "(())()"]),
    (")(", [""]),
    ("(a)())()", ["(a)()()", "(a())()"])
])
def test_solutions(args, expected):
    res = Solution().removeInvalidParentheses(args)
    assert sorted(res) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
