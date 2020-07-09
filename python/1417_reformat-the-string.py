#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个混合了数字和字母的字符串 s，其中的字母均为小写英文字母。 
# 
#  请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。 
# 
#  请你返回 重新格式化后 的字符串；如果无法按要求重新格式化，则返回一个 空字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "a0b1c2"
# 输出："0a1b2c"
# 解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。
#  
# 
#  示例 2： 
# 
#  输入：s = "leetcode"
# 输出：""
# 解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。
#  
# 
#  示例 3： 
# 
#  输入：s = "1229857369"
# 输出：""
# 解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。
#  
# 
#  示例 4： 
# 
#  输入：s = "covid2019"
# 输出："c2o0v1i9d"
#  
# 
#  示例 5： 
# 
#  输入：s = "ab123"
# 输出："1a2b3"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 仅由小写英文字母和/或数字组成。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reformat(self, s: str) -> str:
        """
        AC
        """
        alphas = []
        digits = []
        for char in s:
            if char.isdigit():
                digits.append(char)
            else:
                alphas.append(char)
        if abs(len(alphas) - len(digits)) > 1:
            return ""
        ans = ""
        while alphas and digits:
            ans += alphas.pop()
            ans += digits.pop()
        if digits:
            ans = digits.pop() + ans
        if alphas:
            ans += alphas.pop()
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="a0b1c2"), "0a1b2c"],
    [dict(s="leetcode"), ""],
    [dict(s="1229857369"), ""],
    [dict(s="covid2019"), "c2o0v1i9d"],
    [dict(s="ab123"), "1a2b3"],
])
def test_solutions(kw, expected):
    res = Solution().reformat(**kw)
    if not res:
        assert res == expected
    for a, b in zip(res, res[1:]):
        assert (a.isdigit() and b.isalpha()) or (b.isdigit() and a.isalpha())


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
