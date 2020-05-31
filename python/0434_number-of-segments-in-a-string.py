#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。 
# 
#  请注意，你可以假定字符串里不包括任何不可打印的字符。 
# 
#  示例: 
# 
#  输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
#  
#  Related Topics 字符串

"""
import re

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countSegments(self, s: str) -> int:
        """ 题目不严谨"""
        words = re.split(r"\s+", s)
        return len([x for x in words if x.strip()])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("Hello, my name is John", 5),
    ("Hello, my name is     John", 5),
])
def test_solutions(args, expected):
    assert Solution().countSegments(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
