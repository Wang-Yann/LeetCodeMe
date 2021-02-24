#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 05:56:35
# @Last Modified : 2021-02-24 05:56:35
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。 
# 
#  注意：你 不能 修改非 '?' 字符。 
# 
#  题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。 
# 
#  在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "?zs"
# 输出："azs"
# 解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两
# 个 'z' 。 
# 
#  示例 2： 
# 
#  输入：s = "ubv?w"
# 输出："ubvaw"
# 解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。
#  
# 
#  示例 3： 
# 
#  输入：s = "j?qg??b"
# 输出："jaqgacb"
#  
# 
#  示例 4： 
# 
#  输入：s = "??yw?ipkj?"
# 输出："acywaipkja"
#  
# 
#  
# 
#  提示： 
# 
#  
#  
#  1 <= s.length <= 100 
#  
#  
#  s 仅包含小写英文字母和 '?' 字符 
#  
#  
#  Related Topics 字符串 
#  👍 25 👎 0

"""
import re
import string

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def modifyString(self, s: str) -> str:
        choices = string.ascii_lowercase
        N = len(s)
        chars = list(s)
        for i, char in enumerate(chars):
            if char == "?":
                pre = chars[i - 1] if i != 0 else "|"
                suc = chars[i + 1] if i != N - 1 else "|"
                for choice in choices:
                    if choice != pre and choice != suc:
                        chars[i] = choice
                        break
        return "".join(chars)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def modifyString(self, s: str) -> str:
        res, prev = "", '?'
        for i, c in enumerate(s):
            next = s[i + 1] if i + 1 < len(s) else '?'
            prev = c if c != '?' else {'a', 'b', 'c'}.difference({prev, next}).pop()
            res += prev
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(s="?zs"), "azs"],
    [dict(s="ubv?w"), "ubvaw"],
    [dict(s="j?qg??b"), "jaqgacb"],
    [dict(s="??yw?ipkj?"), "acywaipkja"],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    ans = SolutionCLS().modifyString(**kw)
    assert not re.search(r"([a-z]){2}]", ans)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
