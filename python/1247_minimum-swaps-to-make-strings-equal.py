#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 14:24:00
# @Last Modified : 2020-07-05 14:24:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，你需要通过「交换字符」的方式使这两个字符串相同。 
# 
#  每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。 
# 
#  交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[
# j]。 
# 
#  最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s1 = "xx", s2 = "yy"
# 输出：1
# 解释：
# 交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。 
# 
#  示例 2： 
# 
#  输入：s1 = "xy", s2 = "yx"
# 输出：2
# 解释：
# 交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
# 交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
# 注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。 
# 
#  示例 3： 
# 
#  输入：s1 = "xx", s2 = "xy"
# 输出：-1
#  
# 
#  示例 4： 
# 
#  输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# 输出：4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 1000 
#  s1, s2 只包含 'x' 或 'y'。 
#  
#  Related Topics 贪心算法 字符串 
#  👍 27 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
       Get the count of "x_y" and "y_x"
    If sum of both counts is odd then return -1. We need a pair to make the strings equal
    Each 2 count of "x_y" needs just 1 swap. So add half of "x_y" count to the result
    Each 2 count of "y_x" needs just 1 swap. So add half of "y_x" count to the result
    if we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps so add 2 in result.
   """

    def minimumSwap(self, s1: str, s2: str) -> int:

        x1 = y1 = 0
        N = len(s1)
        for i in range(N):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    x1 += 1
                else:
                    y1 += 1
        if (x1 + y1) % 2 == 1:
            return -1
        res = x1 // 2 + y1 // 2
        if x1 % 2 == 1:
            res += 2
        #  xx, yy needs one swap, and xy yx needs two swaps, so find the pair of x and the number of redundant x
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s1="xx", s2="yy"
    ), 1),
    pytest.param(dict(s1="xy", s2="yx"), 2),
    pytest.param(dict(s1="xx", s2="xy"), -1),
    pytest.param(dict(s1="xxyyxyxyxx", s2="xyyxyxxxyx"), 4),
])
def test_solutions(kwargs, expected):
    assert Solution().minimumSwap(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
