#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s，找出它的所有子串并按字典序排列，返回排在最后的那个子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abab"
# 输出："bab"
# 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab
# "。
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："tcode"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 4 * 10^5 
#  s 仅含有小写英文字符。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastSubstring(self, s: str) -> str:
        """
        GOOD
        首先最大字串肯定是最大后缀字串
       链接：https://leetcode-cn.com/problems/last-substring-in-lexicographical-order/solution/python-shuang-zhi-zhen-362ms-by-mian-mian-sir/

        """
        N, left, right, step = len(s), 0, 1, 0
        while right + step < N:
            if s[right + step] > s[left + step]:
                left, right, step = right, right + 1, 0
            elif s[right + step] < s[left + step]:
                right, step = right + step + 1, 0
            else:
                step += 1
        return s[left:]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("abab", "bab"),
    ("leetcode", "tcode"),
])
def test_solutions(args, expected):
    assert Solution().lastSubstring(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
