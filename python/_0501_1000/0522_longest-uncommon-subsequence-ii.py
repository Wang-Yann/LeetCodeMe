#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。 
# 
#  子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。 
# 
#  输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。 
# 
#  
# 
#  示例： 
# 
#  输入: "aba", "cdc", "eae"
# 输出: 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  所有给定的字符串长度不会超过 10 。 
#  给定字符串列表的长度将在 [2, 50 ] 之间。 
#  
# 
#  
#  Related Topics 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findLUSlength(self, strs: List[str]) -> int:
        """
        先将字符串按长度从大到小进行排序，从长度最长的字符串开始遍历，每个字符串与其后的字符串进行比较，若其后的所有字符串均不是其子串，则该字符串即为最长非公共子串，输出结果，若存在，则结束本次比较，遍历至下一个字符串
        """

        def subseq(w1, w2):
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return len(w1) == i

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not subseq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["aba", "cdc", "eae"], 3),
])
def test_solutions(args, expected):
    assert Solution().findLUSlength(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
