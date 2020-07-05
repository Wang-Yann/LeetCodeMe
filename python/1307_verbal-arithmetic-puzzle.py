#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 19:15:56
# @Last Modified : 2020-07-05 19:15:56
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个方程，左边用 words 表示，右边用 result 表示。 
# 
#  你需要根据以下规则检查方程是否可解： 
# 
#  
#  每个字符都会被解码成一位数字（0 - 9）。 
#  每对不同的字符必须映射到不同的数字。 
#  每个 words[i] 和 result 都会被解码成一个没有前导零的数字。 
#  左侧数字之和（words）等于右侧数字（result）。 
#  
# 
#  如果方程可解，返回 True，否则返回 False。 
# 
#  
# 
#  示例 1： 
# 
#  输入：words = ["SEND","MORE"], result = "MONEY"
# 输出：true
# 解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
# 所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652 
# 
#  示例 2： 
# 
#  输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
# 输出：true
# 解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->
# 4
# 所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214 
# 
#  示例 3： 
# 
#  输入：words = ["THIS","IS","TOO"], result = "FUNNY"
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：words = ["LEET","CODE"], result = "POINT"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= words.length <= 5 
#  1 <= words[i].length, results.length <= 7 
#  words[i], result 只含有大写英文字母 
#  表达式中使用的不同字符数最大为 10 
#  
#  Related Topics 数学 回溯算法 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        HARD
        TODO TODO
        https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463886/Python-backtracking-efficient-column-wise-w-Explanation
        """

        def solve(i, j, carry):
            # print(i,j,carry)
            # The current column assignment is over, so check for validity
            if j == len(words):
                csum = carry
                for k in range(len(words)):
                    csum += 0 if i >= len(words[k]) else assign[words[k][i]]
                    # We have come to column i, but the result itself is not long enough.
                if i >= len(result):
                    return False
                if result[i] in assign:
                    # i th char of result  is already assigned, so check if its valid and go to next column i+1 and start from word 0
                    return csum % 10 == assign[result[i]] and solve(i + 1, 0, csum // 10)
                else:
                    # If the current digit can't be assigned to ith char of result or if its 0 and we are looking at first char of a word: then return False
                    if (csum % 10) in assign.values() or (csum % 10 == 0 and i == len(result) - 1):
                        return False
                assign[result[i]] = csum % 10
                ret = solve(i + 1, 0, csum // 10)
                del assign[result[i]]
                return ret

            if i == len(result):
                return i >= max(len(w) for w in words) and carry == 0 and all(assign[w[len(w) - 1]] != 0 for w in words + [result])
            # Handle length of word less than the column we are looking at OR the ith column char of the jth word is already assigned previously
            if i >= len(words[j]) or words[j][i] in assign:
                return solve(i, j + 1, carry)
            for val in range(10):
                if val == 0 and i == len(words[j]) - 1:
                    continue  # Handle not to assign 0 for first letter of a word
                if val not in assign.values():
                    assign[words[j][i]] = val
                    ret = solve(i, j + 1, carry)
                    if ret:
                        return True
                    del assign[words[j][i]]
            return False

        result = result[::-1]
        words = [w[::-1] for w in words]
        assign = dict()
        return solve(0, 0, 0)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(words=["SEND", "MORE"], result="MONEY"), True),
    pytest.param(dict(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY"), True),
    pytest.param(dict(words=["THIS", "IS", "TOO"], result="FUNNY"), True),
    pytest.param(dict(words=["LEET", "CODE"], result="POINT"), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isSolvable(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
