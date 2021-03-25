#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入： A = "ab", B = "ba"
# 输出： true
#  
# 
#  示例 2： 
# 
#  输入： A = "ab", B = "ab"
# 输出： false
#  
# 
#  示例 3: 
# 
#  输入： A = "aa", B = "aa"
# 输出： true
#  
# 
#  示例 4： 
# 
#  输入： A = "aaaaaaabc", B = "aaaaaaacb"
# 输出： true
#  
# 
#  示例 5： 
# 
#  输入： A = "", B = "aa"
# 输出： false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 20000 
#  0 <= B.length <= 20000 
#  A 和 B 仅由小写字母构成。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def buddyStrings(self, A: str, B: str) -> bool:
        lenA, lenB = map(len, (A, B))
        if lenA != lenB:
            return False
        if A == B:
            return lenA != len(set(A))
        diffA, diffB = [], []
        for i in range(lenA):
            if A[i] != B[i]:
                diffA.append(A[i])
                diffB.append(B[i])
        return len(diffA) == len(diffB) == 2 and diffA == [diffB[1], diffB[0]]

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A="ab", B="ba"), True),
    pytest.param(dict(A="ab", B="ab"), False),
    pytest.param(dict(A="aa", B="aa"), True),
    pytest.param(dict(A="aaaaaaabc", B="aaaaaaacb"), True),
    pytest.param(dict(A="", B="aa"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().buddyStrings(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
