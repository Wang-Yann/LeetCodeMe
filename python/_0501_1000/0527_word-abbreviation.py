#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 18:33:37
# @Last Modified : 2020-07-23 18:33:37
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个由n个不重复非空字符串组成的数组，你需要按照以下规则为每个单词生成最小的缩写。 
# 
#  
#  初始缩写由起始字母+省略字母的数量+结尾字母组成。 
#  若存在冲突，亦即多于一个单词有同样的缩写，则使用更长的前缀代替首字母，直到从单词到缩写的映射唯一。换而言之，最终的缩写必须只能映射到一个单词。 
#  若缩写并不比原单词更短，则保留原样。 
#  
# 
#  示例: 
# 
#  输入: ["like", "god", "internal", "me", "internet", "interval", "intension", "f
# ace", "intrusion"]
# 输出: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
#  
# 
#  
# 
#  注意: 
# 
#  
#  n和每个单词的长度均不超过 400。 
#  每个单词的长度大于 1。 
#  单词只由英文小写字母组成。 
#  返回的答案需要和原数组保持同一顺序。 
#  
#  Related Topics 排序 字符串 
#  👍 14 👎 0

"""

import collections
from typing import List

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
Trie = lambda: collections.defaultdict(Trie)


class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        """
        分组 + 最短公共前缀
        """
        words = dict
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [""] * len(words)
        COUNT = "#"
        i = 0
        for group in groups.values():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1:
                        break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word) - i - 1) + word[-1]
                else:
                    ans[index] = word
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def wordsAbbreviation(self, words):
        """贪心"""

        def abbrev(word, i=0):
            if len(word) - i <= 3:
                return word
            return word[:i + 1] + str(len(word) - i - 2) + word[-1]

        N = len(words)
        ans = list(map(abbrev, words))
        prefix = [0] * N

        for i in range(N):
            while True:
                dupes = set()
                for j in range(i + 1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes:
                    break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(words[k], prefix[k])

        return ans


@pytest.mark.parametrize("args,expected", [
    (
            ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"],
            ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"]
    )
])
def test_solutions(args, expected):
    assert Solution().wordsAbbreviation(args) == expected
    assert Solution1().wordsAbbreviation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
