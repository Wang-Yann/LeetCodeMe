#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 13:47:46
# @Last Modified : 2020-07-23 13:47:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。 
# 
#  示例 1: 
# 
#  输入: s = "eceba", k = 2
# 输出: 3
# 解释: 则 T 为 "ece"，所以长度为 3。 
# 
#  示例 2: 
# 
#  输入: s = "aa", k = 1
# 输出: 2
# 解释: 则 T 为 "aa"，所以长度为 2。
#  
#  Related Topics 哈希表 字符串 Sliding Window 
#  👍 48 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """AC"""
        window = collections.Counter()
        l = ans = 0
        N = len(s)
        for r in range(N):
            window[s[r]] += 1
            while len(window) > k:
                char = s[l]
                window[char] -= 1
                if window[char] == 0:
                    window.pop(char)
                l += 1
            ans = max(ans, r - l + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="eceba", k=2), 3],
    [dict(s="aa", k=1), 2],
])
def test_solutions(kw, expected):
    assert Solution().lengthOfLongestSubstringKDistinct(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
