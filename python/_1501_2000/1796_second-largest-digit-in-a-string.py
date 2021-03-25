#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-22 03:11:36
# @Last Modified : 2021-03-22 03:11:36
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。 
# 
#  混合字符串 由小写英文字母和数字组成。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母和（或）数字。 
#  
#  Related Topics 字符串 
#  👍 1 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def secondHighest(self, s: str) -> int:
        first = sec = -1
        for c in s:
            if c.isdigit():
                num = ord(c) - ord('0')
                if first < num:
                    sec, first = first, num
                elif sec < num < first:
                    sec = num
        return sec


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def secondHighest(self, s: str) -> int:
        nums = sorted({int(char) for char in s if char.isdigit()}, reverse=True)
        return -1 if len(nums) <= 1 else nums[1]


@pytest.mark.parametrize("kw,expected", [
    [dict(s="dfa12321afd"), 2],
    [dict(s="abc1111"), -1],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().secondHighest(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
