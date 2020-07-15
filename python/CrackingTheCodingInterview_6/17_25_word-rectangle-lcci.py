#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 15:06:11
# @Last Modified : 2020-07-15 15:06:11
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单
# 里连续出现，但要求所有行等长，所有列等高。 
# 
#  如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。 
# 
#  示例 1: 
# 
#  输入: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 输出:
# [
#   "this",
#   "real",
#   "hard"
# ] 
# 
#  示例 2: 
# 
#  输入: ["aa"]
# 输出: ["aa","aa"] 
# 
#  说明： 
# 
#  
#  words.length <= 1000 
#  words[i].length <= 100 
#  数据保证单词足够随机 
#  
#  👍 5 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.root = [{}, False]

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur[0]:
                cur[0][c] = [{}, False]
            cur = cur[0][c]
        cur[1] = True


class Solution:
    def maxRectangle(self, words: List[str]) -> List[str]:
        self.area = 0
        self.res = []
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(trie_arr, path):
            # print(trie_arr, path,"\n")
            for word in words:
                if len(word) != len(trie_arr):
                    continue
                for i, char in enumerate(word):
                    if char not in trie_arr[i][0]:
                        break
                else:
                    temp = trie_arr[:]
                    flag = True
                    for i, char in enumerate(word):
                        temp[i] = temp[i][0][char]
                        flag &= temp[i][1]
                    path.append(word)
                    if flag:
                        h, w = len(path), len(word)
                        if h * w > self.area:
                            self.area = h * w
                            self.res = path[:]
                    dfs(temp, path)
                    path.pop()

        ll = sorted(set(map(len, words)), reverse=True)
        for l in ll:
            if l * ll[0] < self.area:
                break
            dfs([trie.root] * l, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(words=["this", "real", "hard", "trh", "hea", "iar", "sld"]), ["this", "real", "hard"]],
    [dict(words=["aa"]), ["aa", "aa"]],
])
def test_solutions(kw, expected):
    assert Solution().maxRectangle(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
