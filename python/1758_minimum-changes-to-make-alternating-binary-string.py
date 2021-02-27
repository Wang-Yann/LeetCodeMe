#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 19:26:58
# @Last Modified : 2021-02-27 19:26:58
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个仅由字符 '0' 和 '1' 组成的字符串 s 。一步操作中，你可以将任一 '0' 变成 '1' ，或者将 '1' 变成 '0' 。 
# 
#  交替字符串 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 "010" 是交替字符串，而字符串 "0100" 
# 不是。 
# 
#  返回使 s 变成 交替字符串 所需的 最少 操作数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "0100"
# 输出：1
# 解释：如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。
#  
# 
#  示例 2： 
# 
#  输入：s = "10"
# 输出：0
# 解释：s 已经是交替字符串。
#  
# 
#  示例 3： 
# 
#  输入：s = "1111"
# 输出：2
# 解释：需要 2 步操作得到 "0101" 或 "1010" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s[i] 是 '0' 或 '1' 
#  
#  Related Topics 贪心算法 数组 
#  👍 10 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minOperations(self, s: str) -> int:
        b0 = b1 = 0
        b0_char, b1char = "0", "1"
        for char in s:
            if char != b0_char:
                b0 += 1
            elif char != b1char:
                b1 += 1
            b0_char, b1char = b1char, b0_char
        return min(b0, b1)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def minOperations(self, s):
        res = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(res, len(s) - res)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="0100"), 1],
    [dict(s="10"), 0],
    [dict(s="1111"), 2],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minOperations(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
