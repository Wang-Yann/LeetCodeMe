#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 10:22:56
# @Last Modified : 2020-08-07 10:22:56
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个近义词表 synonyms 和一个句子 text ， synonyms 表中是一些近义词对 ，你可以将句子 text 中每个单词用它的近义词来替换。
#  
# 
#  请你找出所有用近义词替换后的句子，按 字典序排序 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
# text = "I am happy today but was sad yesterday"
# 输出：
# ["I am cheerful today but was sad yesterday",
# "I am cheerful today but was sorrow yesterday",
# "I am happy today but was sad yesterday",
# "I am happy today but was sorrow yesterday",
# "I am joy today but was sad yesterday",
# "I am joy today but was sorrow yesterday"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= synonyms.length <= 10 
#  synonyms[i].length == 2 
#  synonyms[0] != synonyms[1] 
#  所有单词仅包含英文字母，且长度最多为 10 。 
#  text 最多包含 10 个单词，且单词间用单个空格分隔开。 
#  
#  Related Topics 回溯算法 
#  👍 12 👎 0

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        """AC"""
        groups = []
        for a, b in synonyms:
            for a_set in groups:
                if a in a_set or b in a_set:
                    a_set.update({a, b})
                    continue
            groups.append({a, b})

        lookup = {}
        for i, a_set in enumerate(groups):
            for w in a_set:
                lookup[w] = i
        ans = set()
        words = text.split()
        N = len(words)

        def backtrack(idx, path):
            if idx == N:
                ans.add(" ".join(path))
                return
            cur_word = words[idx]
            backtrack(idx + 1, path + [cur_word])
            if cur_word in lookup:
                candidates = groups[lookup[cur_word]]
                for candidate in candidates:
                    backtrack(idx + 1, path + [candidate])

        backtrack(0, [])
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        synonyms=[["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]],
        text="I am happy today but was sad yesterday"
    ),
        ["I am cheerful today but was sad yesterday",
         "I am cheerful today but was sorrow yesterday",
         "I am happy today but was sad yesterday",
         "I am happy today but was sorrow yesterday",
         "I am joy today but was sad yesterday",
         "I am joy today but was sorrow yesterday"]

    ],
])
def test_solutions(kw, expected):
    assert Solution().generateSentences(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
