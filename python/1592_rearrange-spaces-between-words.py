#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 08:11:01
# @Last Modified : 2021-02-24 08:11:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 
# text 至少包含一个单词 。 
# 
#  请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也
# 意味着返回的字符串应当与原 text 字符串的长度相等。 
# 
#  返回 重新排列空格后的字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：text = "  this   is  a sentence "
# 输出："this   is   a   sentence"
# 解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。
#  
# 
#  示例 2： 
# 
#  输入：text = " practice   makes   perfect"
# 输出："practice   makes   perfect "
# 解释：总共有 7 个空格和 3 个单词。7 / (3-1) = 3 个空格加上 1 个多余的空格。多余的空格需要放在字符串的末尾。
#  
# 
#  示例 3： 
# 
#  输入：text = "hello   world"
# 输出："hello   world"
#  
# 
#  示例 4： 
# 
#  输入：text = "  walks  udp package   into  bar a"
# 输出："walks  udp  package  into  bar  a "
#  
# 
#  示例 5： 
# 
#  输入：text = "a"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 100 
#  text 由小写英文字母和 ' ' 组成 
#  text 中至少包含一个单词 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""
import re

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_cnt = text.count(" ")
        words = re.split(r"\s+", text.strip(" "))
        # print(words)
        N = len(words)
        if N == 1:
            return words[0] + " " * space_cnt
        quotient, rest = divmod(space_cnt, N - 1)
        return (" " * quotient).join(words) + " " * rest


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(text="  this   is  a sentence "), "this   is   a   sentence"],
    [dict(text=" practice   makes   perfect"), "practice   makes   perfect "],
    [dict(text="hello   world"), "hello   world"],
    [dict(text="  walks  udp package   into  bar a"), "walks  udp  package  into  bar  a "],
    [dict(text="a"), "a"],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().reorderSpaces(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
