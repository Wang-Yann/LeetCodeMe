#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。） 
# 
#  如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。 
# 
#  返回所有不常用单词的列表。 
# 
#  您可以按任何顺序返回列表。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet","sour"]
#  
# 
#  示例 2： 
# 
#  输入：A = "apple apple", B = "banana"
# 输出：["banana"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 200 
#  0 <= B.length <= 200 
#  A 和 B 都只包含空格和小写字母。 
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):

    def uncommonFromSentences(self, A, B):
        count = collections.Counter(A.split())
        count += collections.Counter(B.split())
        return [word for word in count if count[word] == 1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        counterA = collections.Counter(A.split())
        counterB = collections.Counter(B.split())
        ans = []
        for word, cnt in counterA.items():
            if cnt == 1 and counterB[word] == 0:
                ans.append(word)
        for word, cnt in counterB.items():
            if cnt == 1 and counterA[word] == 0:
                ans.append(word)
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A="this apple is sweet", B="this apple is sour"
    ), ["sweet", "sour"]),
    pytest.param(dict(A="apple apple", B="banana"), ["banana"]),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().uncommonFromSentences(**kwargs)) == sorted(expected)
    assert sorted(Solution1().uncommonFromSentences(**kwargs)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
