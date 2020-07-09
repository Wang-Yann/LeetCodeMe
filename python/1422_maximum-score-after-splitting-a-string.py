#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。 
# 
# 
#  「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "011101"
# 输出：5 
# 解释：
# 将字符串 s 划分为两个非空子字符串的可行方案有：
# 左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5 
# 左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4 
# 左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3 
# 左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2 
# 左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3
#  
# 
#  示例 2： 
# 
#  输入：s = "00111"
# 输出：5
# 解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5
#  
# 
#  示例 3： 
# 
#  输入：s = "1111"
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= s.length <= 500 
#  字符串 s 仅由字符 '0' 和 '1' 组成。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = s.count('1', 1)  # count '1's in s[1:]
        score = zeros + ones
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros + ones, score)
        return score


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def maxScore(self, s: str) -> int:
        """AC"""
        ans = 0
        left = 0
        right = s.count("1")
        for char in s[:-1]:
            if char == "0":
                left += 1
            else:
                right -= 1
            ans = max(ans, left + right)
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(s="011101"), 5],
    [dict(s="00111"), 5],
    [dict(s="1111"), 3],
    [dict(s="00"), 1],
    [dict(s="11"), 1],
])
def test_solutions(kw, expected):
    assert Solution().maxScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
