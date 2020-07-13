#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:11:09
# @Last Modified : 2020-07-13 11:11:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  例如，给出 n = 3，生成结果为： 
# 
#  
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 28 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(l, r, s):
            if l == r == n:
                ans.append(s)
            if l < n:
                dfs(l + 1, r, s + '(')
            if r < l:
                dfs(l, r + 1, s + ')')

        dfs(0, 0, '')
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(n=3),
     [
         "((()))",
         "(()())",
         "(())()",
         "()(())",
         "()()()"
     ]
     ],
])
def test_solutions(kw, expected):
    assert Solution().generateParenthesis(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
