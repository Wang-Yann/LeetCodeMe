#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 16:21:06
# @Last Modified : 2020-07-21 16:21:06
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。 
# 
#  注意： 
# 
#  满足编辑距离等于 1 有三种可能的情形： 
# 
#  
#  往 s 中插入一个字符得到 t 
#  从 s 中删除一个字符得到 t 
#  在 s 中替换一个字符得到 t 
#  
# 
#  示例 1： 
# 
#  输入: s = "ab", t = "acb"
# 输出: true
# 解释: 可以将 'c' 插入字符串 s 来得到 t。
#  
# 
#  示例 2: 
# 
#  输入: s = "cab", t = "ad"
# 输出: false
# 解释: 无法通过 1 步操作使 s 变为 t。 
# 
#  示例 3: 
# 
#  输入: s = "1203", t = "1213"
# 输出: true
# 解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。 
#  Related Topics 字符串 
#  👍 27 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # The strings are NOT one edit away distance
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings have the same length
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                # if strings have different lengths
                else:
                    return s[i:] == t[i + 1:]

        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character.
        return ns + 1 == nt


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="ab", t="acb"), True],
    [dict(s="cab", t="ad"), False],
    [dict(s="1203", t="1213"), True],
])
def test_solutions(kw, expected):
    assert Solution().isOneEditDistance(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
