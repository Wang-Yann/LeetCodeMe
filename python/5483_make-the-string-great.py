#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 12:30:49
# @Last Modified : 2020-08-09 12:30:49
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由大小写英文字母组成的字符串 s 。 
# 
#  一个整理好的字符串中，两个相邻字符 s[i] 和 s[i + 1] 不会同时满足下述条件： 
# 
#  
#  0 <= i <= s.length - 2 
#  s[i] 是小写字符，但 s[i + 1] 是相同的大写字符；反之亦然 。 
#  
# 
#  请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 两个相邻 字符并删除，直到字符串整理好为止。 
# 
#  请返回整理好的 字符串 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。 
# 
#  注意：空字符串也属于整理好的字符串，尽管其中没有任何字符。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "leEeetcode"
# 输出："leetcode"
# 解释：无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "abBAcC"
# 输出：""
# 解释：存在多种不同情况，但所有的情况都会导致相同的结果。例如：
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
#  
# 
#  示例 3： 
# 
#  输入：s = "s"
# 输出："s"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含小写和大写英文字母 
#  
#  Related Topics 栈 字符串 
#  👍 0 👎 0
	 

"""

import pytest,traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeGood(self, s: str) -> str:
        chars = list(s)
        need_change = True
        while need_change:
            new_chars = []
            i = 0
            need_change = False
            while i < len(chars):
                if i + 1 < len(chars) and chars[i].lower() == chars[i + 1].lower() and chars[i] != chars[i + 1]:
                    i += 2
                    need_change = True
                else:
                    new_chars.append(chars[i])
                    i += 1
            chars = new_chars
        return "".join(chars)
# leetcode submit region end(Prohibit modification and deletion)


# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="leEeetcode"), "leetcode"],
    pytest.param(dict(s="abBAcC"), ""),
    pytest.param(dict(s="s"), "s"),
    pytest.param(dict(s=""), ""),
    pytest.param(dict(s="Ss"), ""),
])
def test_solutions1(kwargs, expected):
    assert Solution().makeGood(**kwargs) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])