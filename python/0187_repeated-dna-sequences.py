#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究
# 非常有帮助。 
# 
#  编写一个函数来查找 DNA 分子中所有出现超过一次的 10 个字母长的序列（子串）。 
# 
#  
# 
#  示例： 
# 
#  输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"] 
#  Related Topics 位运算 哈希表

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        length = len(s)
        counter =collections.Counter()
        if length<10:
            return []
        for i in range(length-10+1):
            counter[s[i:i+10]]+=1
        return [x for x,y in counter.items() if y>1]

# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"] ),
    ("AAAAAAAAAAA", ["AAAAAAAAAA"] ),
])
def test_solutions(args, expected):
    res= Solution().findRepeatedDnaSequences(args)
    assert sorted(res) == sorted(expected)




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])