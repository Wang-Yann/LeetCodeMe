#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。 
# 
#  示例 1: 
# 
#  
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#  
# 
#  说明: 
# 
#  
#  字符串 S 的长度范围为 [1, 10000]。 
#  C 是一个单字符，且保证是字符串 S 里的字符。 
#  S 和 C 中的所有字母均为小写字母。 
#  
# 

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = [0] * len(S)
        indexes = set()
        for idx, char in enumerate(S):
            if char == C:
                indexes.add(idx)
        for i, char in enumerate(S):
            if i not in indexes:
                ans[i] = min(abs(i - pos) for pos in indexes)
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        S="loveleetcode", C='e'
    ), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
])
def test_solutions(kwargs, expected):
    assert Solution().shortestToChar(**kwargs) == expected
    assert Solution1().shortestToChar(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
