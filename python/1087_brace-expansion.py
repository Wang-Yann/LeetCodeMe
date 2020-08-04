#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 15:17:57
# @Last Modified : 2020-08-04 15:17:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们用一个特殊的字符串 S 来表示一份单词列表，之所以能展开成为一个列表，是因为这个字符串 S 中存在一个叫做「选项」的概念： 
# 
#  单词中的每个字母可能只有一个选项或存在多个备选项。如果只有一个选项，那么该字母按原样表示。 
# 
#  如果存在多个选项，就会以花括号包裹来表示这些选项（使它们与其他字母分隔开），例如 "{a,b,c}" 表示 ["a", "b", "c"]。 
# 
#  例子："{a,b,c}d{e,f}" 可以表示单词列表 ["ade", "adf", "bde", "bdf", "cde", "cdf"]。 
# 
#  请你按字典顺序，返回所有以这种方式形成的单词。 
# 
#  
# 
#  示例 1： 
# 
#  输入："{a,b}c{d,e}f"
# 输出：["acdf","acef","bcdf","bcef"]
#  
# 
#  示例 2： 
# 
#  输入："abcd"
# 输出：["abcd"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 50 
#  你可以假设题目中不存在嵌套的花括号 
#  在一对连续的花括号（开花括号与闭花括号）之间的所有字母都不会相同 
#  
#  Related Topics 回溯算法 
#  👍 17 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def expand(self, S: str) -> List[str]:
        """AC"""
        ans = []
        N = len(S)
        brackets = {}
        l = None
        for i in range(N):
            if S[i] == "{":
                l = i
            elif S[i] == "}":
                brackets[l] = i

        def dfs(cur, path):
            if cur == N:
                ans.append(path)
                return
            if S[cur] == "{":
                j = brackets[cur]
                chars = S[cur + 1:j].split(",")
                for char in chars:
                    dfs(j + 1, path + char)
            elif S[cur].isalpha():
                dfs(cur + 1, path + S[cur])

        dfs(0, "")
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(S="{a,b}c{d,e}f"), ["acdf", "acef", "bcdf", "bcef"]],
    [dict(S="abcd"), ["abcd"]],
    [dict(S="{a,b}{z,x,y}"), ['ax', 'ay', 'az', 'bx', 'by', 'bz']],
])
def test_solutions(kw, expected):
    assert Solution().expand(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
