#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。 
# 
#  返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有： 
# 
#  
#  如果 S[i] == "I"，那么 A[i] < A[i+1] 
#  如果 S[i] == "D"，那么 A[i] > A[i+1] 
#  
# 
#  
# 
#  示例 1： 
# 
#  输出："IDID"
# 输出：[0,4,1,3,2]
#  
# 
#  示例 2： 
# 
#  输出："III"
# 输出：[0,1,2,3]
#  
# 
#  示例 3： 
# 
#  输出："DDI"
# 输出：[3,2,0,1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 10000 
#  S 只包含字符 "I" 或 "D"。 
#  
#  Related Topics 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        ans = []
        l, r = 0, N
        for char in S:
            if char == "I":
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        ans.append(l)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def diStringMatch(self, S: str) -> List[int]:
        N = len(S)
        candidates = list(range(N+1))
        ans = []
        for char in S:
            if char == "I":
                ans.append(candidates.pop(0))
            else:
                ans.append(candidates.pop())
        return ans+candidates




@pytest.mark.parametrize("args,expected", [
    ("IDID", [0, 4, 1, 3, 2]),
    pytest.param("III", [0, 1, 2, 3]),
    pytest.param("DDI", [3, 2, 0, 1]),
])
def test_solutions(args, expected):
    assert Solution().diStringMatch(args) == expected
    assert Solution1().diStringMatch(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
