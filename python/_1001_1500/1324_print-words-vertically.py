#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-06 23:22:10
# @Last Modified : 2020-07-06 23:22:10
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个字符串 s。请你按照单词在 s 中的出现顺序将它们全部竖直返回。 
# 单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。 
# 每个单词只能放在一列上，每一列中也只能有一个单词。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "HOW ARE YOU"
# 输出：["HAY","ORO","WEU"]
# 解释：每个单词都应该竖直打印。 
#  "HAY"
#  "ORO"
#  "WEU"
#  
# 
#  示例 2： 
# 
#  输入：s = "TO BE OR NOT TO BE"
# 输出：["TBONTB","OEROOE","   T"]
# 解释：题目允许使用空格补位，但不允许输出末尾出现空格。
# "TBONTB"
# "OEROOE"
# "   T"
#  
# 
#  示例 3： 
# 
#  输入：s = "CONTEST IS COMING"
# 输出：["CIC","OSO","N M","T I","E N","S G","T"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 200 
#  s 仅含大写英文字母。 
#  题目数据保证两个单词之间只有一个空格。 
#  
#  Related Topics 字符串 
#  👍 20 👎 0

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools
from common_utils import TreeNode,ListNode
from sample_datas import BIG_CASE,BIG_RES







# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def printVertically(self, s: str) -> List[str]:
        """
        对于我们返回的字符串列表，它的长度等于最长的单词长度，其中每个元素的长度等于单词的数量
        """
        words = s.split()
        # print(words,list(itertools.zip_longest(*words,fillvalue=" ")))
        return ["".join(char).rstrip() for char in itertools.zip_longest(*words,fillvalue=" ")]

        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s = "HOW ARE YOU"
    ), ["HAY","ORO","WEU"]),
    pytest.param(dict( s = "TO BE OR NOT TO BE"  ), ["TBONTB","OEROOE","   T"]),
    pytest.param(dict( s = "CONTEST IS COMING"), ["CIC","OSO","N M","T I","E N","S G","T"]),
])
def test_solutions(kwargs, expected):
    assert Solution().printVertically(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])

