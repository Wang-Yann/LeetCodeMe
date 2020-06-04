#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以 s 看起来是这样的："...zabcdefghijklm
# nopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....". 
# 
#  现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同
# 的非空子串的数目。 
# 
#  注意: p 仅由小写的英文字母组成，p 的大小可能超过 10000。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: "a"
# 输出: 1
# 解释: 字符串 S 中只有一个"a"子字符。
#  
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: "cac"
# 输出: 2
# 解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.
#  
# 
#  
# 
#  示例 3: 
# 
#  
# 输入: "zab"
# 输出: 6
# 解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。.
#  
# 
#  
#  Related Topics 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findSubstringInWraproundString(self, p: str) -> int:
        """
        动态规划来维护以每一个字母为末尾的最长子串长度
        """
        res = dict.fromkeys(p, 1)
        l = 1
        for i, j in zip(p, p[1:]):
            if (ord(j) - ord(i)) % 26 == 1:
                l += 1
            else:
                l = 1
            res[j] = max(res[j], l)
        # print(res)
        return sum(res.values())


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("a", 1),
    ("zab", 6),
    pytest.param("cac", 2),
])
def test_solutions(args, expected):
    assert Solution().findSubstringInWraproundString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
