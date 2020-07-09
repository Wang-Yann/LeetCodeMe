#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数： 
# 
#  
#  子串中不同字母的数目必须小于等于 maxLetters 。 
#  子串的长度必须大于等于 minSize 且小于等于 maxSize 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# 输出：2
# 解释：子串 "aab" 在原字符串中出现了 2 次。
# 它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
#  
# 
#  示例 2： 
# 
#  输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# 输出：2
# 解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
#  
# 
#  示例 3： 
# 
#  输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# 输出：3
#  
# 
#  示例 4： 
# 
#  输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  1 <= maxLetters <= 26 
#  1 <= minSize <= maxSize <= min(26, s.length) 
#  s 只包含小写英文字母。 
#  
#  Related Topics 位运算 字符串

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # Time:  O(m * n), m = 26
    # Space: O(m * n)
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        lookup = collections.Counter()
        N = len(s)
        for right in range(minSize - 1, N):
            word = s[right - minSize + 1:right + 1]
            if word in lookup:
                lookup[word] += 1
            elif len(collections.Counter(word)) <= maxLetters:
                lookup[word] += 1
        return max(lookup.values() or [0])


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
       (Rabin-Karp Algorithm
        """
        MOD, BASE = 10 ** 9 + 7, 31
        power, rolling_hash = pow(BASE, minSize - 1, MOD), 0

        left = 0
        lookup, count = collections.defaultdict(int), collections.defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            if right - left + 1 > minSize:
                count[s[left]] -= 1
                rolling_hash = (rolling_hash - ord(s[left]) * power) % MOD
                if count[s[left]] == 0:
                    count.pop(s[left])
                left += 1
            rolling_hash = (rolling_hash * BASE + ord(s[right])) % MOD
            if right - left + 1 == minSize and len(count) <= maxLetters:
                lookup[rolling_hash] += 1
        return max(lookup.values() or [0])


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aababcaab", maxLetters=2, minSize=3, maxSize=4), 2],
    [dict(s="aaaa", maxLetters=1, minSize=3, maxSize=3), 2],
    [dict(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3), 3],
    [dict(s="abcde", maxLetters=2, minSize=3, maxSize=3), 0],
])
def test_solutions(kw, expected):
    assert Solution().maxFreq(**kw) == expected
    assert Solution1().maxFreq(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])