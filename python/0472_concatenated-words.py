#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。 
# 
#  连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。 
# 
#  示例: 
# 
#  
# 输入: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","rat
# catdogcat"]
# 
# 输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# 解释: "catsdogcats"由"cats", "dog" 和 "cats"组成; 
#      "dogcatsdog"由"dog", "cats"和"dog"组成; 
#      "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
#  
# 
#  说明: 
# 
#  
#  给定数组的元素总数不超过 10000。 
#  给定数组中元素的长度总和不超过 600000。 
#  所有输入字符串只包含小写字母。 
#  不需要考虑答案输出的顺序。 
#  
#  Related Topics 深度优先搜索 字典树 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """TODO"""
        words.sort(key=len)
        min_len = max(1, len(words[0]))
        prev = set()
        res = []

        def check(word):
            if word in prev: return True
            for i in range(min_len, len(word) - min_len + 1):
                if word[:i] in prev and check(word[i:]):
                    return True
            return False

        for word in words:
            if check(word):
                res.append(word)
            prev.add(word)
        return res


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        TODO TODO
        """
        trie = {}
        for word in words:
            if not word:
                continue
            cur = trie
            for char in word:
                cur = cur.setdefault(char, {})
            cur["#"] = "#"
        res = []

        def dfs(word, idx, cnt, cur_trie):
            # 组成个数 > 2, 并且以#结束的
            if idx == len(word):
                return cnt >= 1 and "#" in cur_trie
            if "#" in cur_trie:
                if dfs(word, idx, cnt + 1, trie):
                    return True
            if word[idx] not in cur_trie:
                return False
            if dfs(word, idx + 1, cnt, cur_trie[word[idx]]):
                return True
            return False

        for word in words:
            # 参数分别为, 单词word, 位置idx, 目前为止有几个单词组成了cnt, 字典树trie
            if dfs(word, 0, 0, trie):
                res.append(word)
        return res


@pytest.mark.parametrize("args,expected", [
    (["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
     ["catsdogcats", "dogcatsdog", "ratcatdogcat"]
     )
])
def test_solutions(args, expected):
    assert sorted(Solution().findAllConcatenatedWordsInADict(args)) == sorted(expected)
    assert sorted(Solution1().findAllConcatenatedWordsInADict(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
