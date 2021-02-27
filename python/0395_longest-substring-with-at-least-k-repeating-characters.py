#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。 
# 
#  示例 1: 
# 
#  
# 输入:
# s = "aaabb", k = 3
# 
# 输出:
# 3
# 
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s = "ababbc", k = 2
# 
# 输出:
# 5
# 
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
#  
# 

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """HARD"""

    def longestSubstring(self, s: str, k: int) -> int:
        def helper(start, end):

            counter = collections.Counter(s[start:end])
            max_len = 0
            l = start
            while l < end:
                while l < end and counter[s[l]] < k:
                    l += 1
                r = l
                while r < end and counter[s[r]] >= k:
                    r += 1
                if l == start and r == end:
                    return end - start
                max_len = max(max_len, helper(l, r))
                l = r
            return max_len

        return helper(0, len(s))


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """分治"""

    def longestSubstring(self, s: str, k: int) -> int:
        length = len(s)
        if length < k:
            return 0
        t = min(set(s), key=s.count)
        if s.count(t) >= k:
            return length
        return max(self.longestSubstring(sub_s, k) for sub_s in s.split(t))


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="aaabb", k=3), 3),
    pytest.param(dict(s="ababbc", k=2), 5),
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().longestSubstring(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
