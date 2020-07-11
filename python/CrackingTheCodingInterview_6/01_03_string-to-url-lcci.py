#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:29:51
# @Last Modified : 2020-07-11 23:29:51
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，
# 请使用字符数组实现，以便直接在数组上操作。） 
# 
#  示例1: 
# 
#   输入："Mr John Smith    ", 13
#  输出："Mr%20John%20Smith"
#  
# 
#  示例2: 
# 
#   输入："               ", 5
#  输出："%20%20%20%20%20"
#  
# 
#  提示： 
# 
#  
#  字符串长度在[0, 500000]范围内。 
#  
#  Related Topics 字符串 
#  👍 12 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("args,expected", [
    (
            ["Mr John Smith    ", 13]
            , "Mr%20John%20Smith"),
    pytest.param(["               ", 5], "%20%20%20%20%20"),
])
def test_solutions(args, expected):
    assert Solution().replaceSpaces(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
