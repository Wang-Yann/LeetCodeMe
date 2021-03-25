#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在给定单词列表 wordlist 的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。 
# 
#  对于给定的查询单词 query，拼写检查器将会处理两类拼写错误： 
# 
#  
#  大小写：如果查询匹配单词列表中的某个单词（不区分大小写），则返回的正确单词与单词列表中的大小写相同。
# 
#  
#  例如：wordlist = ["yellow"], query = "YellOw": correct = "yellow" 
#  例如：wordlist = ["Yellow"], query = "yellow": correct = "Yellow" 
#  例如：wordlist = ["yellow"], query = "yellow": correct = "yellow" 
#  
#  
#  元音错误：如果在将查询单词中的元音（‘a’、‘e’、‘i’、‘o’、‘u’）分别替换为任何元音后，能与单词列表中的单词匹配（不区分大小写），则返回的正确单
# 词与单词列表中的匹配项大小写相同。
#  
#  例如：wordlist = ["YellOw"], query = "yollow": correct = "YellOw" 
#  例如：wordlist = ["YellOw"], query = "yeellow": correct = "" （无匹配项） 
#  例如：wordlist = ["YellOw"], query = "yllw": correct = "" （无匹配项） 
#  
#  
#  
# 
#  此外，拼写检查器还按照以下优先级规则操作： 
# 
#  
#  当查询完全匹配单词列表中的某个单词（区分大小写）时，应返回相同的单词。 
#  当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。 
#  当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。 
#  如果该查询在单词列表中没有匹配项，则应返回空字符串。 
#  
# 
#  给出一些查询 queries，返回一个单词列表 answer，其中 answer[i] 是由查询 query = queries[i] 得到的正确单词。 
# 
# 
#  
# 
#  示例： 
# 
#  输入：wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe",
# "Hare","HARE","Hear","hear","keti","keet","keto"]
# 输出：["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= wordlist.length <= 5000 
#  1 <= queries.length <= 5000 
#  1 <= wordlist[i].length <= 7 
#  1 <= queries[i].length <= 7 
#  wordlist 和 queries 中的所有字符串仅由英文字母组成。 
#  
#  Related Topics 哈希表 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        在所有 3 种情况下，我们都可以使用哈希表来查询答案。

        对于第一种情况（完全匹配），我们使用集合存放单词以有效地测试查询单词是否在该组中。
        对于第二种情况（大小写不同），我们使用一个哈希表，该哈希表将单词从其小写形式转换为原始单词（大小写正确的形式）。
        对于第三种情况（元音错误），我们使用一个哈希表，将单词从其小写形式（忽略元音的情况下）转换为原始单词。
        该算法仅剩的要求是认真规划和仔细阅读问题。

        """
        VOWELS = set("aeiou")

        def todev(word):
            return "".join("*" if c.lower() in VOWELS else c.lower() for c in word)

        words = set(wordlist)
        caps = {}
        vows = {}
        for word in wordlist:
            caps.setdefault(word.lower(), word)
            vows.setdefault(todev(word), word)

        def solve(query):
            if query in words:
                return query
            lower = query.lower()
            if lower in caps:
                return caps[lower]
            devow = todev(lower)
            if devow in vows:
                return vows[devow]
            return ""

        return list(map(solve, queries))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(wordlist=["KiTe", "kite", "hare", "Hare"],
          queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]
          ),
     ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]],
])
def test_solutions(kw, expected):
    assert Solution().spellchecker(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
