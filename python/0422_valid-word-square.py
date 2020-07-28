#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 18:20:16
# @Last Modified : 2020-07-28 18:20:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个单词序列，判断其是否形成了一个有效的单词方块。 
# 
#  有效的单词方块是指此由单词序列组成的文字方块的 第 k 行 和 第 k 列 (0 ≤ k < max(行数, 列数)) 所显示的字符串完全相同。 
# 
#  注意： 
# 
#  
#  给定的单词数大于等于 1 且不超过 500。 
#  单词长度大于等于 1 且不超过 500。 
#  每个单词只包含小写英文字母 a-z。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
# 
# 输出：
# true
# 
# 解释：
# 第 1 行和第 1 列都是 "abcd"。
# 第 2 行和第 2 列都是 "bnrt"。
# 第 3 行和第 3 列都是 "crmy"。
# 第 4 行和第 4 列都是 "dtye"。
# 
# 因此，这是一个有效的单词方块。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
# 
# 输出：
# true
# 
# 解释：
# 第 1 行和第 1 列都是 "abcd"。
# 第 2 行和第 2 列都是 "bnrt"。
# 第 3 行和第 3 列都是 "crm"。
# 第 4 行和第 4 列都是 "dt"。
# 
# 因此，这是一个有效的单词方块。
#  
# 
#  
# 
#  示例 3： 
# 
#  输入：
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
# 
# 输出：
# false
# 
# 解释：
# 第 3 行是 "read" ，然而第 3 列是 "lead"。
# 
# 因此，这 不是 一个有效的单词方块。
#  
# 
#  
#  👍 15 👎 0

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != words[i][j]:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return False
        # R,C=len(words),max(map(len,words))
        transfer = []
        for w in itertools.zip_longest(*words, fillvalue=""):
            transfer.append("".join(w))
        return transfer == words


@pytest.mark.parametrize("args,expected", [
    (
            [
                "abcd",
                "bnrt",
                "crmy",
                "dtye"
            ], True
    ),
    (
            [
                "abcd",
                "bnrt",
                "crm",
                "dt"
            ], True

    ), (

            [
                "ball",
                "area",
                "read",
                "lady"
            ], False

    )
])
def test_solutions(args, expected):
    assert Solution().validWordSquare(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
