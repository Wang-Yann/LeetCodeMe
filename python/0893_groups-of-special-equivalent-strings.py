#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 你将得到一个字符串数组 A。 
# 
#  如果经过任意次数的移动，S == T，那么两个字符串 S 和 T 是特殊等价的。 
# 
#  一次移动包括选择两个索引 i 和 j，且 i ％ 2 == j ％ 2，交换 S[j] 和 S [i]。 
# 
#  现在规定，A 中的特殊等价字符串组是 A 的非空子集 S，这样不在 S 中的任何字符串与 S 中的任何字符串都不是特殊等价的。 
# 
#  返回 A 中特殊等价字符串组的数量。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：["a","b","c","a","c","c"]
# 输出：3
# 解释：3 组 ["a","a"]，["b"]，["c","c","c"]
#  
# 
#  示例 2： 
# 
#  输入：["aa","bb","ab","ba"]
# 输出：4
# 解释：4 组 ["aa"]，["bb"]，["ab"]，["ba"]
#  
# 
#  示例 3： 
# 
#  输入：["abc","acb","bac","bca","cab","cba"]
# 输出：3
# 解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
#  
# 
#  示例 4： 
# 
#  输入：["abcd","cdab","adcb","cbad"]
# 输出：1
# 解释：1 组 ["abcd","cdab","adcb","cbad"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 1000 
#  1 <= A[i].length <= 20 
#  所有 A[i] 都具有相同的长度。 
#  所有 A[i] 都只由小写字母组成。 
#  
#  Related Topics 字符串

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def transfer(word):
            odd = tuple(sorted(word[::2]))
            even = tuple(sorted(word[1::2]))
            return odd,even

        groups = set(map(transfer,A))
        return len(groups)
        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["a","b","c","a","c","c"],3),
    pytest.param(["aa","bb","ab","ba"], 4),
    pytest.param(["abcd","cdab","adcb","cbad"], 1),
])
def test_solutions(args, expected):
    assert Solution().numSpecialEquivGroups(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

