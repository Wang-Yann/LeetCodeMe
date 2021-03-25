#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个长度相同的字符串，s 和 t。 
# 
#  将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的
# 绝对值。 
# 
#  用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。 
# 
#  如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。 
# 
#  如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcd", t = "bcdf", cost = 3
# 输出：3
# 解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。 
# 
#  示例 2： 
# 
#  输入：s = "abcd", t = "cdef", cost = 3
# 输出：1
# 解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
#  
# 
#  示例 3： 
# 
#  输入：s = "abcd", t = "acde", cost = 0
# 输出：1
# 解释：你无法作出任何改动，所以最大长度为 1。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10^5 
#  0 <= maxCost <= 10^6 
#  s 和 t 都只含小写英文字母。 
#  
#  Related Topics 数组 Sliding Window

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        20200616　纪念一下
        掌握滑动窗114
        """
        ans = 0
        l = 0
        window = 0
        for r, (sc, tc) in enumerate(zip(s, t)):
            window += abs(ord(sc) - ord(tc))
            while window > maxCost:
                window -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            # print(l, r, sc, tc, )
            ans = max(ans, r - l + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abcd", t="bcdf", maxCost=3), 3],
    [dict(s="abcd", t="cdef", maxCost=3), 1],
    [dict(s="abcd", t="acde", maxCost=0), 1],
])
def test_solutions(kw, expected):
    assert Solution().equalSubstring(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
