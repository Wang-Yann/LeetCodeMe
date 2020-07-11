#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:35:05
# @Last Modified : 2020-07-11 23:35:05
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。 
# 
#  示例1: 
# 
#   输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
#  
# 
#  示例2: 
# 
#   输入：s1 = "aa", s2 = "aba"
#  输出：False
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  字符串长度在[0, 100000]范围内。 
#  
# 
#  说明: 
# 
#  
#  你能只调用一次检查子串的方法吗？ 
#  
#  Related Topics 字符串 
#  👍 28 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1)==len(s2) and s2 in s1 + s1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s1="waterbottle", s2="erbottlewat"), True],

    pytest.param(dict(s1="aa", s2="aba"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isFlipedString(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
