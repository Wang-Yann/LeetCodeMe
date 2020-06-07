#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符： 
# 
#  
#  'A' : Absent，缺勤 
#  'L' : Late，迟到 
#  'P' : Present，到场 
#  
# 
#  如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。 
# 
#  你需要根据这个学生的出勤记录判断他是否会被奖赏。 
# 
#  示例 1: 
# 
#  输入: "PPALLP"
# 输出: True
#  
# 
#  示例 2: 
# 
#  输入: "PPALLL"
# 输出: False
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def checkRecord(self, s: str) -> bool:
        count_A = 0
        for i in range(len(s)):
            if s[i] == 'A':
                count_A += 1
                if count_A == 2:
                    return False
            if i < len(s) - 2 and s[i] == s[i + 1] == s[i + 2] == 'L':
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def checkRecord(self, s: str) -> bool:
        exceed_2L = False
        cnt_A = 0
        cur_2L = 0
        for i in range(len(s)):
            if s[i] == "A":
                cnt_A += 1
            if s[i] == "L":
                cur_2L += 1
                if cur_2L > 2:
                    exceed_2L = True
            else:
                cur_2L = 0
        return cnt_A <= 1 and not exceed_2L


@pytest.mark.parametrize("args,expected", [
    ("PPALLP", True),
    pytest.param("PPALLL", False),
])
def test_solutions(args, expected):
    assert Solution().checkRecord(args) == expected
    assert Solution1().checkRecord(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
