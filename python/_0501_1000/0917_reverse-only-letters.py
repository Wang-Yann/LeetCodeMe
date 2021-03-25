#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入："ab-cd"
# 输出："dc-ba"
#  
# 
#  示例 2： 
# 
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  示例 3： 
# 
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S 中不包含 \ or " 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def reverseOnlyLetters(self, S: str) -> str:
        lst = list(S)
        l, r = 0, len(S) - 1
        while l <= r:
            while l <= r and not lst[l].isalpha():
                l += 1
            while l <= r and not lst[r].isalpha():
                r -= 1
            if l <= r:
                # print(l,r)
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
        return "".join(lst)


@pytest.mark.parametrize("args,expected", [
    ("ab-cd", "dc-ba"),
    pytest.param("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
    pytest.param("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),
])
def test_solutions(args, expected):
    assert Solution().reverseOnlyLetters(args) == expected
    assert Solution1().reverseOnlyLetters(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
