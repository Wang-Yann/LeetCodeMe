#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。 
# 
#  你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。 
# 
#  要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。 
# 
#  文本的最后一行应为左对齐，且单词之间不插入额外的空格。 
# 
#  说明: 
# 
#  
#  单词是指由非空格字符组成的字符序列。 
#  每个单词的长度大于 0，小于等于 maxWidth。 
#  输入单词数组 words 至少包含一个单词。 
#  
# 
#  示例: 
# 
#  输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
# "This is an",
# "example of text",
# "justification. "
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# 输出:
# [
# "What must be",
# "acknowledgment ",
# "shall be "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
#    因为最后一行应为左对齐，而不是左右两端对齐。       
#      第二行同样为左对齐，这是因为这行只包含一个单词。
#  
# 
#  示例 3: 
# 
#  输入:
# words = ["Science","is","what","we","understand","well","enough","to","explain
# ",
#        "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# 输出:
# [
# "Science is what we",
#   "understand well",
# "enough to explain to",
# "a computer. Art is",
# "everything else we",
# "do "
# ]
#  
#  Related Topics 字符串

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def format_line(line):
            words_cnt = len(line)
            if words_cnt == 1:
                return line[0] + " " * (maxWidth - len(line[0]))
            len_sum = sum([len(word) for word in line])
            s, gaps = line[0], words_cnt - 1
            for index, w in enumerate(line[1:]):
                average_gaps_cnt = ((maxWidth - len_sum) // gaps)
                if index < (maxWidth - len_sum) % gaps:
                    s = s + " " + " " * average_gaps_cnt + w
                else:
                    s = s + " " * average_gaps_cnt + w
            return s

        def format_last(line):
            s = " ".join(line)
            return s + " " * (maxWidth - len(s))

        line, length = [], 0
        res = []
        for w in words:
            if length + len(w) + len(line) <= maxWidth:
                length += len(w)
                line.append(w)
            else:
                res.append(format_line(line))
                length = len(w)
                line = [w]
        if len(line):
            res.append(format_last(line))
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16
    ), [
         "This    is    an",
         "example  of text",
         "justification.  "
     ]),
    (dict(
        words=["What", "must", "be", "acknowledgment", "shall", "be"],
        maxWidth=16
    ), [
         "What   must   be",
         "acknowledgment  ",
         "shall be        "
     ]),
    (dict(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
               "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
        maxWidth=20
    ), [
         "Science  is  what we",
         "understand      well",
         "enough to explain to",
         "a  computer.  Art is",
         "everything  else  we",
         "do                  "
     ]
    )

])
def test_solutions(kwargs, expected):
    assert Solution().fullJustify(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
