#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 22:01:25
# @Last Modified : 2020-04-08 22:01:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
#  注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#
#
#  示例 1：
#
#  输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
#  示例 2：
#
#  输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]
#
#  Related Topics 哈希表 双指针 字符串
#  👍 297 👎 0

"""
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (s and words): return []
        res = []
        words.sort()
        lws, ls = len(words), len(s)
        lw = len(words[0])
        for i in range(ls - lw * lws + 1):
            if self.checkExistAll(words, s[i:i + lw * lws], lws, lw):
                res.append(i)
        return res

    def checkExistAll(self, words, s, lws, lw):
        tmp_list = []
        for i in range(lws):
            word = s[i * lw:(i + 1) * lw]
            if word in words:
                tmp_list.append(word)
            else:
                return False

        return sorted(tmp_list) == words


if __name__ == '__main__':
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(sol.findSubstring(s, words))
