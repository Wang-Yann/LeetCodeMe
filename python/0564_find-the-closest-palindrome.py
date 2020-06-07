#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数 n ，你需要找到与它最近的回文数（不包括自身）。 
# 
#  “最近的”定义为两个整数差的绝对值最小。 
# 
#  示例 1: 
# 
#  
# 输入: "123"
# 输出: "121"
#  
# 
#  注意: 
# 
#  
#  n 是由字符串表示的正整数，其长度不超过18。 
#  如果有多个结果，返回最小的那个。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = {str(10 ** length + 1), str(10 ** (length - 1) - 1)}
        prefix = int(n[:(length + 1) // 2])
        for half in map(str, [prefix - 1, prefix, prefix + 1]):
            if length & 0b1:
                candidates.add(half + half[:-1][::-1])
            else:
                candidates.add(half + half[::-1])
        candidates.discard(n)
        key_func = lambda x:(abs(int(x) - int(n)), int(x))
        return min(candidates, key= key_func)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("123", "121"),
    ("21", "22"),
    ("1", "0"),
    ("99", "101"),
])
def test_solutions(args, expected):
    assert Solution().nearestPalindromic(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
