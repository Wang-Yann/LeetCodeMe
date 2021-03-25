#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定两个字符串, A 和 B。 
# 
#  A 的旋转操作就是将 A 最左边的字符移动到最右边。 例如, 若 A = 'abcde'，在移动一次之后结果就是'bcdea' 。如果在若干次旋转操作之后
# ，A 能变成B，那么返回True。 
# 
#  
# 示例 1:
# 输入: A = 'abcde', B = 'cdeab'
# 输出: true
# 
# 示例 2:
# 输入: A = 'abcde', B = 'abced'
# 输出: false 
# 
#  注意： 
# 
#  
#  A 和 B 长度不超过 100。 
#  
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        lenA, lenB = len(A), len(B)
        if lenA != lenB:
            return False
        BB = B + B
        for i in range(lenA):
            if BB[i:].startswith(A):
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    def rotateString(self, A, B):
        return len(A) == len(B) and B in A * 2


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A='abcde', B='cdeab'
    ), True),
    pytest.param(dict(A='abcde', B='abced'), False),
])
def test_solutions(kwargs, expected):
    assert Solution().rotateString(**kwargs) == expected
    assert Solution1().rotateString(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
