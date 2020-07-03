#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s 中（按字典序比较）最小字母的出现频次。 
# 
#  例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。 
# 
#  现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 
# f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。 
# 
#  
# 
#  示例 1： 
# 
#  输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
#  
# 
#  示例 2： 
# 
#  输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= queries.length <= 2000 
#  1 <= words.length <= 2000 
#  1 <= queries[i].length, words[i].length <= 10 
#  queries[i][j], words[i][j] 都是小写英文字母 
#  
#  Related Topics 数组 字符串

"""
import bisect
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_values = [sum(char == min(word) for char in word) for word in words]
        queries_values = [sum(char == min(word) for char in word) for word in queries]
        words_counter = collections.Counter(words_values)
        ans = [0] * len(queries)
        for i, v in enumerate(queries_values):
            v = sum(words_counter[i] for i in range(v + 1, 10 + 1))
            ans[i] = v
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    """GOOD"""
    def numSmallerByFrequency(self, queries, words):
        words_freq = sorted(word.count(min(word)) for word in words)
        return [len(words) - bisect.bisect_right(words_freq, query.count(min(query))) for query in queries]


@pytest.mark.parametrize("kw,expected", [
    [dict(queries=["cbd"], words=["zaaaz"]), [1]],
    [dict(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]), [1, 2]],
])
def test_solutions(kw, expected):
    assert Solution().numSmallerByFrequency(**kw) == expected
    assert Solution1().numSmallerByFrequency(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
