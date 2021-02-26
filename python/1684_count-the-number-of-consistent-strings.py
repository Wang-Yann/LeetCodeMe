#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 03:28:32
# @Last Modified : 2021-02-26 03:28:33
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字
# 符串 。 
# 
#  请你返回 words 数组中 一致字符串 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# 输出：2
# 解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。
#  
# 
#  示例 2： 
# 
#  
# 输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
# 输出：7
# 解释：所有字符串都是一致的。
#  
# 
#  示例 3： 
# 
#  
# 输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
# 输出：4
# 解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= words.length <= 104 
#  1 <= allowed.length <= 26 
#  1 <= words[i].length <= 10 
#  allowed 中的字符 互不相同 。 
#  words[i] 和 allowed 只包含小写英文字母。 
#  
#  Related Topics 字符串 
#  👍 7 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        return sum(all(char in allowed_set for char in word) for word in words)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]), 2],
    [dict(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"]), 7],
    [dict(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]), 4],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countConsistentStrings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
