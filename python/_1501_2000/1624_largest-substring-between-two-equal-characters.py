#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 02:57:55
# @Last Modified : 2021-02-25 02:57:55
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。 
# 
#  子字符串 是字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aa"
# 输出：0
# 解释：最优的子字符串是两个 'a' 之间的空子字符串。 
# 
#  示例 2： 
# 
#  输入：s = "abca"
# 输出：2
# 解释：最优的子字符串是 "bc" 。
#  
# 
#  示例 3： 
# 
#  输入：s = "cbzxy"
# 输出：-1
# 解释：s 中不存在出现出现两次的字符，所以返回 -1 。
#  
# 
#  示例 4： 
# 
#  输入：s = "cabbac"
# 输出：4
# 解释：最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 300 
#  s 只含小写英文字母 
#  
#  Related Topics 字符串 
#  👍 8 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        lookup = {}
        ans = -1
        for i, char in enumerate(s):
            if char in lookup:
                ans = max(ans, i - lookup[char] - 1)
            else:
                lookup[char] = i
        return ans

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aa"), 0],
    [dict(s="abca"), 2],
    [dict(s="cbzxy"), -1],
    [dict(s="cabbac"), 4],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxLengthBetweenEqualCharacters(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
