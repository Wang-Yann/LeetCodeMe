#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面
# 的字符构成。如果可以构成，返回 true ；否则返回 false。 
# 
#  (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。) 
# 
#  
# 
#  注意： 
# 
#  你可以假设两个字符串均只含有小写字母。 
# 
#  canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#  
#  Related Topics 字符串

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        targets = collections.Counter(ransomNote)
        source = collections.Counter(magazine)
        for char, cnt in targets.items():
            if source[char] < cnt:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

class Solution2(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)


@pytest.mark.parametrize("args,expected", [
    (("a", "b"), False),
    (("aa", "aab"), True),
    pytest.param(("aa", "ab"), False),
])
def test_solutions(args, expected):
    assert Solution().canConstruct(*args) == expected
    assert Solution2().canConstruct(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
