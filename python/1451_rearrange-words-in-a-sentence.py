#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 09:52:48
# @Last Modified : 2020-07-10 09:52:49
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text : 
# 
#  
#  句子的首字母大写 
#  text 中的每个单词都用单个空格分隔。 
#  
# 
#  请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。 
# 
#  请同样按上述格式返回新的句子。 
# 
#  
# 
#  示例 1： 
# 
#  输入：text = "Leetcode is cool"
# 输出："Is cool leetcode"
# 解释：句子中共有 3 个单词，长度为 8 的 "Leetcode" ，长度为 2 的 "is" 以及长度为 4 的 "cool" 。
# 输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。
#  
# 
#  示例 2： 
# 
#  输入：text = "Keep calm and code on"
# 输出："On and keep calm code"
# 解释：输出的排序情况如下：
# "On" 2 个字母。
# "and" 3 个字母。
# "keep" 4 个字母，因为存在长度相同的其他单词，所以它们之间需要保留在原句子中的相对顺序。
# "calm" 4 个字母。
# "code" 4 个字母。
#  
# 
#  示例 3： 
# 
#  输入：text = "To be or not to be"
# 输出："To be or to be not"
#  
# 
#  
# 
#  提示： 
# 
#  
#  text 以大写字母开头，然后包含若干小写字母以及单词间的单个空格。 
#  1 <= text.length <= 10^5 
#  
#  Related Topics 排序 字符串 
#  👍 5 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words.sort(key=len)
        return " ".join(words).capitalize()


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(text="Leetcode is cool"), "Is cool leetcode"],
    [dict(text="Keep calm and code on"), "On and keep calm code"],
    [dict(text="To be or not to be"), "To be or to be not"],
])
def test_solutions(kw, expected):
    assert Solution().arrangeWords(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
