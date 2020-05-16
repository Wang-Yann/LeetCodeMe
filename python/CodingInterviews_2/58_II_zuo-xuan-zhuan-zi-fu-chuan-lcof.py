#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数
# 将返回左旋转两位得到的结果"cdefgab"。 
# 
#  
# 
#  示例 1： 
# 
#  输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
#  
# 
#  示例 2： 
# 
#  输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= k < s.length <= 10000 
#  
#  Related Topics 字符串

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, n + len(s)):
            res.append(s[i % len(s)])
        return ''.join(res)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="abcdefg", n=2), "cdefgab"),
    pytest.param(dict(s="lrloseumgh", n=6), "umghlrlose"),
])
def test_solutions(kwargs, expected):
    assert Solution().reverseLeftWords(**kwargs) == expected
    assert Solution1().reverseLeftWords(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
