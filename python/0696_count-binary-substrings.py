#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。 
# 
#  重复出现的子串要计算它们出现的次数。 
# 
#  示例 1 : 
# 
#  
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
# 
# 请注意，一些重复出现的子串要计算它们出现的次数。
# 
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#  
# 
#  示例 2 : 
# 
#  
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#  
# 
#  注意： 
# 
#  
#  s.length 在1到50,000之间。 
#  s 只包含“0”或“1”字符。 
#  
#  Related Topics 字符串

"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode/
        按字符分组
        让我们创建上面定义的 groups。s 的第一个元素属于它自己的组。
        每个元素要么与前一个元素不匹配，从而开始一个大小为 1 的新组；要么匹配，从而使最近一个组的大小增加 1。
        然后，我们将取 min(groups[i-1], groups[i]) 的和

        """
        groups = [list(vs) for k, vs in itertools.groupby(s)]
        lens = list(map(len, groups))
        ans = 0
        for a, b in zip(lens, lens[1:]):
            ans += min(a, b)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("00110011", 6),
    ("10101", 4),
])
def test_solutions(args, expected):
    assert Solution().countBinarySubstrings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
