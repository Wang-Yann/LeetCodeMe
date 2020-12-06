#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 s 和 t，判断它们是否是同构的。 
# 
#  如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。 
# 
#  所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。 
# 
#  示例 1: 
# 
#  输入: s = "egg", t = "add"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "foo", t = "bar"
# 输出: false 
# 
#  示例 3: 
# 
#  输入: s = "paper", t = "title"
# 输出: true 
# 
#  说明: 
# 你可以假设 s 和 t 具有相同的长度。 
#  Related Topics 哈希表

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:


        NS, NT = map(len, (s, t))
        if NS != NT:
            return False
        s2t,t2s = {},{}
        for sw,tw in zip(s,t):
            if tw not in s2t and sw not in t2s:
                s2t[tw]=sw
                t2s[sw]=tw
            elif tw not in s2t or s2t[tw]!=sw:
                # Contradict mapping.
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def isIsomorphic(self, s: str, t: str) -> bool:

        def helper(s, t):
            lookup = {}
            for x, y in zip(s, t):
                if x not in lookup:
                    lookup[x] = y
                    continue
                if lookup[x] != y:
                    return False
            return True

        length_s, length_t = map(len, (s, t))
        if length_s != length_t:
            return False
        return helper(s, t) and helper(t, s)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="egg", t="add"), True),
    pytest.param(dict(s="foo", t="bar"), False),
    pytest.param(dict(s="paper", t="title"), True),
    pytest.param(dict(s="ab", t="aa"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isIsomorphic(**kwargs) == expected
    assert Solution1().isIsomorphic(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
