#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 13:48:58
# @Last Modified : 2020-07-15 13:48:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。 
# 
#  编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。 
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# ["hit","hot","dot","lot","log","cog"]
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。 
#  Related Topics 深度优先搜索 广度优先搜索 数组 字符串 
#  👍 16 👎 0

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        picture_dic = collections.defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                picture_dic[word[:i] + '*' + word[i + 1:]].add(word)

        self.res = []

        # print(picture_dic)

        def dfs(cur, path, seen):
            if cur == endWord:
                self.res = path
                return

            for i in range(len(cur)):
                for word in picture_dic[cur[:i] + '*' + cur[i + 1:]]:
                    if word not in seen:
                        seen.add(word)
                        dfs(word, path + [word], seen)

        dfs(beginWord, [beginWord], {beginWord})

        return self.res

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]

    ), ["hit", "hot", "dot", "lot", "log", "cog"]],
    [dict(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log"]

    ), []],
])
def test_solutions(kw, expected):
    res = Solution().findLadders(**kw)
    assert res == expected or res[0] == kw["beginWord"] and res[-1] == kw["endWord"]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
