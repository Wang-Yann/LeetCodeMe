#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 17:50:20
# @Last Modified : 2020-07-28 17:50:20
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 rows x cols 的屏幕和一个用 非空 的单词列表组成的句子，请你计算出给定句子可以在屏幕上完整显示的次数。 
# 
#  注意： 
# 
#  
#  一个单词不能拆分成两行。 
#  单词在句子中的顺序必须保持不变。 
#  在一行中 的两个连续单词必须用一个空格符分隔。 
#  句子中的单词总量不会超过 100。 
#  每个单词的长度大于 0 且不会超过 10。 
#  1 ≤ rows, cols ≤ 20,000. 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：
# rows = 2, cols = 8, 句子 sentence = ["hello", "world"]
# 
# 输出：
# 1
# 
# 解释：
# hello---
# world---
# 
# 字符 '-' 表示屏幕上的一个空白位置。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：
# rows = 3, cols = 6, 句子 sentence = ["a", "bcd", "e"]
# 
# 输出：
# 2
# 
# 解释：
# a-bcd- 
# e-a---
# bcd-e-
# 
# 字符 '-' 表示屏幕上的一个空白位置。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：
# rows = 4, cols = 5, 句子 sentence = ["I", "had", "apple", "pie"]
# 
# 输出：
# 1
# 
# 解释：
# I-had
# apple
# pie-I
# had--
# 
# 字符 '-' 表示屏幕上的一个空白位置。
#  
# 
#  
#  Related Topics 动态规划 
#  👍 28 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        """GOOD"""
        all_str = ""
        for word in sentence:
            all_str += word + " "
        start, N = 0, len(all_str)
        for i in range(rows):
            start += cols
            if all_str[start % N] == " ":
                start += 1
            else:
                while start > 0 and all_str[(start - 1) % N] != " ":
                    start -= 1
        # print("'%s'"%all_str,N,start)
        return start // N


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(rows=2, cols=8, sentence=["hello", "world"]), 1],
    [dict(rows=3, cols=6, sentence=["a", "bcd", "e"]), 2],
    [dict(rows=4, cols=5, sentence=["I", "had", "apple", "pie"]), 1],
])
def test_solutions(kw, expected):
    assert Solution().wordsTyping(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
