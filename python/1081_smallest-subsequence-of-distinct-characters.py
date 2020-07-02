#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 返回字符串 text 中按字典序排列最小的子序列，该子序列包含 text 中所有不同字符一次。 
# 
#  
# 
#  示例 1： 
# 
#  输入："cdadabcc"
# 输出："adbc"
#  
# 
#  示例 2： 
# 
#  输入："abcd"
# 输出："abcd"
#  
# 
#  示例 3： 
# 
#  输入："ecbacba"
# 输出："eacb"
#  
# 
#  示例 4： 
# 
#  输入："leetcode"
# 输出："letcod"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 1000 
#  text 由小写英文字母组成 
#  
# 
#  
# 
#  注意：本题目与 316 https://leetcode-cn.com/problems/remove-duplicate-letters/ 相同 
#  Related Topics 字符串

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-6/
    """

    def smallestSubsequence(self, text: str) -> str:
        stack = []
        remain_counter = collections.Counter(text)
        lookup = set()
        for char in text:
            if char not in lookup:
                while stack and char < stack[-1] and remain_counter[stack[-1]] > 0:
                    lookup.discard(stack.pop())
                stack.append(char)
                lookup.add(char)
            remain_counter[char] -= 1
        return "".join(stack)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("cdadabcc", "adbc"),
    ("abcd", "abcd"),
    ("ecbacba", "eacb"),
    ("leetcode", "letcod"),
])
def test_solutions(args, expected):
    assert Solution().smallestSubsequence(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
