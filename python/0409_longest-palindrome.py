#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。 
# 
#  在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。 
# 
#  注意: 
# 假设字符串的长度不会超过 1010。 
# 
#  示例 1: 
# 
#  
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#  
#  Related Topics 哈希表

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestPalindrome(self, s: str) -> int:
        odds = 0
        for k, v in collections.Counter(s).items():
            odds += v & 1
        return len(s) - odds + int(odds > 0)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("abccccdd", 7),
])
def test_solutions(args, expected):
    assert Solution().longestPalindrome(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
