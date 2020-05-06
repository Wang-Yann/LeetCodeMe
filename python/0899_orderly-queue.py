#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出了一个由小写字母组成的字符串 S。然后，我们可以进行任意次数的移动。 
# 
#  在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。 
# 
#  返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "cba", K = 1
# 输出："acb"
# 解释：
# 在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
# 在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。
#  
# 
#  示例 2： 
# 
#  输入：S = "baaca", K = 3
# 输出："aaabc"
# 解释：
# 在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
# 在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= K <= S.length <= 1000 
#  S 只由小写字母组成。 
#  
#  Related Topics 数学 字符串

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K==1:
            return min(S[i:]+S[:i] for i in range(len(S)))
        return "".join(sorted(S))


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(S="cba", K=1), "acb"],
    [dict(S="baaca", K=3), "aaabc"],
])
def test_solutions(kw, expected):
    assert Solution().orderlyQueue(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
