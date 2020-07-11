#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:32:05
# @Last Modified : 2020-07-11 23:32:05
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没
# 有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。 
# 
#  示例1: 
# 
#  
#  输入："aabcccccaaa"
#  输出："a2b1c5a3"
#  
# 
#  示例2: 
# 
#  
#  输入："abbccd"
#  输出："abbccd"
#  解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
#  
# 
#  提示： 
# 
#  
#  字符串长度在[0, 50000]范围内。 
#  
#  Related Topics 字符串 
#  👍 45 👎 0


"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def compressString(self, S: str) -> str:
        new_s = ""
        N = len(S)
        for char, grp in itertools.groupby(S):
            new_s += "%s%d" % (char, len(list(grp)))
        return new_s if len(new_s) < N else S


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    ("aabcccccaaa", "a2b1c5a3"),
    pytest.param("abbccd", "abbccd"),
])
def test_solutions(args, expected):
    assert Solution().compressString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
