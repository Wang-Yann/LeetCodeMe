#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 11:41:12
# @Last Modified : 2020-07-10 11:41:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个二进制字符串 s 和一个整数 k 。 
# 
#  如果所有长度为 k 的二进制字符串都是 s 的子串，请返回 True ，否则请返回 False 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "00110110", k = 2
# 输出：true
# 解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
#  
# 
#  示例 2： 
# 
#  输入：s = "00110", k = 2
# 输出：true
#  
# 
#  示例 3： 
# 
#  输入：s = "0110", k = 1
# 输出：true
# 解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
#  
# 
#  示例 4： 
# 
#  输入：s = "0110", k = 2
# 输出：false
# 解释：长度为 2 的二进制串 "00" 没有出现在 s 中。
#  
# 
#  示例 5： 
# 
#  输入：s = "0000000001011100", k = 4
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 5 * 10^5 
#  s 中只含 0 和 1 。 
#  1 <= k <= 20 
#  
#  Related Topics 位运算 字符串 
#  👍 11 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        学着点
        """
        return len({s[i:i + k] for i in range(len(s) - k + 1)}) == 2 ** k


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="00110110", k=2), True],
    [dict(s="00110", k=2), True],
    [dict(s="0110", k=1), True],
    [dict(s="0110", k=2), False],
    [dict(s="0000000001011100", k=4), False],
    [dict(s=("0100100010011110100101010111010001000101110001110010010101000000110101010"
             "111010010001101011010100001111111111110100001001000000100011111100111001000"
             "00010110100011101000100010100011100101110110101101011101101100110100010010"
             "00110001101010101010111011111000010110101101100010000001001110000000000001"
             "100110111001011010100101001011111110010010001100011100101110111001100101001011100001110"),
          k=7), False]
])
def test_solutions(kw, expected):
    assert Solution().hasAllCodes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
