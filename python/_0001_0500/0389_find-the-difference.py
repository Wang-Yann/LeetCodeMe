#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个字符串 s 和 t，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例: 
# 
#  输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
#  
#  Related Topics 位运算 哈希表

"""
import collections
import functools
import operator

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findTheDifference(self, s: str, t: str) -> str:
        return chr(functools.reduce(operator.xor, map(ord, s + t)))


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def findTheDifference(self, s: str, t: str) -> str:
        res = (collections.Counter(t) - collections.Counter(s))
        return list(res.keys()).pop()


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s="abcd",
        t="abcde"
    ), "e"),
])
def test_solutions(kwargs, expected):
    assert Solution().findTheDifference(**kwargs) == expected
    assert Solution1().findTheDifference(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
