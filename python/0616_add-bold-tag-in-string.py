#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 16:11:51
# @Last Modified : 2020-07-30 16:11:51
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给一个字符串 s 和一个字符串列表 dict ，你需要将在字符串列表中出现过的 s 的子串添加加粗闭合标签 <b> 和 </b> 。如果两个子串有重叠部分，
# 你需要把它们一起用一个闭合标签包围起来。同理，如果两个子字符串连续被加粗，那么你也需要把它们合起来用一个加粗标签包围。 
# 
#  样例 1： 
# 
#  输入：
# s = "abcxyz123"
# dict = ["abc","123"]
# 输出：
# "<b>abc</b>xyz<b>123</b>"
#  
# 
#  
# 
#  样例 2： 
# 
#  输入：
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# 输出：
# "<b>aaabbc</b>c"
#  
# 
#  
# 
#  注意： 
# 
#  
#  给定的 dict 中不会有重复的字符串，且字符串数目不会超过 100 。 
#  输入中的所有字符串长度都在范围 [1, 1000] 内。 
#  
# 
#  
#  Related Topics 字符串 
#  👍 27 👎 0

"""
import collections
import functools
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        """
        我们枚举 dict 中的每一个单词 word，并枚举 s 中的位置 i，如果 s[i] 以 word 为前缀，那么我们就在 s 中找到了一个 word 出现的位置。
        我们把 word 占有的所有位置都打上标记，mask[i] == true 表示 s 的位置 i 被打上标记。

        在打完所有的标记后，我们得到了 mask 数组，接下来我们要用这个数组得到加粗的字符串。对于 s 中的位置 i，
        如果 i == 0（字符串的起始位置）或者 mask[i] == true && mask[i - 1] == false，
        那么 i 就是加粗标签的开始位置；如果 i == N - 1 或者 mask[i] == true && mask[i + 1] == false，
        那么 i 就是加粗标签的结束位置。在我们找到了所有的开始和结束位置之后，在这些位置插入 <b> 和 </b> 标签，就得到了加粗的字符串。

        """
        N = len(s)
        mask = [False] * N
        for i in range(N):
            prefix = s[i:]
            for word in dict:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), N)):
                        mask[j] = True
        # print(mask)
        ans = []
        # """TODO groupby"""
        for incl, grp in itertools.groupby(zip(s, mask), lambda x: x[1]):
            # print(incl,list(grp))
            if incl:
                ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl:
                ans.append("</b>")
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def addBoldTag(self, s, words):

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for i, word in enumerate(words):
            functools.reduce(dict.__getitem__, word, trie).setdefault("_end")

        lookup = [False] * len(s)
        for i in range(len(s)):
            curr = trie
            k = -1
            for j in range(i, len(s)):
                if s[j] not in curr:
                    break
                curr = curr[s[j]]
                if "_end" in curr:
                    k = j
            for j in range(i, k + 1):
                lookup[j] = True

        result = []
        for i in range(len(s)):
            if lookup[i] and (i == 0 or not lookup[i - 1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s) - 1 or not lookup[i + 1]):
                result.append("</b>")
        return "".join(result)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        s="abcxyz123",
        dict=["abc", "123"]
    ), "<b>abc</b>xyz<b>123</b>"],
    [dict(
        s="aaabbcc",
        dict=["aaa", "aab", "bc"]
    ), "<b>aaabbc</b>c"
    ],
])
def test_solutions(kw, expected):
    assert Solution().addBoldTag(**kw) == expected
    assert Solution1().addBoldTag(kw["s"], kw["dict"]) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
