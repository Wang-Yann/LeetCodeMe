#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-19 06:53:59
# @Last Modified : 2021-03-19 06:53:59
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你长度相等的两个字符串 s1 和 s2 。一次 字符串交换 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。 
# 
#  如果对 其中一个字符串 执行 最多一次字符串交换 就可以使两个字符串相等，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s1 = "bank", s2 = "kanb"
# 输出：true
# 解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"
#  
# 
#  示例 2： 
# 
#  输入：s1 = "attack", s2 = "defend"
# 输出：false
# 解释：一次字符串交换无法使两个字符串相等
#  
# 
#  示例 3： 
# 
#  输入：s1 = "kelb", s2 = "kelb"
# 输出：true
# 解释：两个字符串已经相等，所以不需要进行字符串交换
#  
# 
#  示例 4： 
# 
#  输入：s1 = "abcd", s2 = "dcba"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 100 
#  s1.length == s2.length 
#  s1 和 s2 仅由小写英文字母组成 
#  
#  Related Topics 字符串 
#  👍 8 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        N = len(s1)
        diff = [s1[i] + s2[i] for i in range(N) if s1[i] != s2[i]]
        return not diff or (len(diff) == 2 and diff[0] == diff[1][::-1])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s1="bank", s2="kanb"), True],
    [dict(s1="attack", s2="defend"), False],
    [dict(s1="kelb", s2="kelb"), True],
    [dict(s1="abcd", s2="dcba"), False],
    [dict(s1="aa", s2="ac"), False],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().areAlmostEqual(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
