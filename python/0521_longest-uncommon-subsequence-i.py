#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你两个字符串，请你从这两个字符串中找出最长的特殊序列。 
# 
#  「最长特殊序列」定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。 
# 
#  子序列 可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。 
# 
#  输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入: "aba", "cdc"
# 输出: 3
# 解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。 
# 
#  示例 2： 
# 
#  输入：a = "aaa", b = "bbb"
# 输出：3
#  
# 
#  示例 3： 
# 
#  输入：a = "aaa", b = "aaa"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  两个字符串长度均处于区间 [1 - 100] 。 
#  字符串中的字符仅含有 'a'~'z' 。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(a="aba", b="cdc"), 3),
    pytest.param(dict(a="aaa", b="bbb"), 3),
    pytest.param(dict(a="aaa", b="aaa"), -1),
    pytest.param(dict(a="aefawfawfawfaw", b="aefawfeawfwafwaef"), 17),
])
def test_solutions(kwargs, expected):
    assert Solution().findLUSlength(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
