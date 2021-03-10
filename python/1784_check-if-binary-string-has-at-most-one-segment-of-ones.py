#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-10 08:22:09
# @Last Modified : 2021-03-10 08:22:11
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个二进制字符串 s ，该字符串 不含前导零 。 
# 
#  如果 s 最多包含 一个由连续的 '1' 组成的字段 ，返回 true 。否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "1001"
# 输出：false
# 解释：字符串中的 1 没有形成一个连续字段。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "110"
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s[i] 为 '0' 或 '1' 
#  s[0] 为 '1' 
#  
#  Related Topics 贪心算法 
#  👍 5 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """阅读理解?"""
        return "01" not in s


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="1001"), False],
    [dict(s="110"), True],
    [dict(s="1"), True],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().checkOnesSegment(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
