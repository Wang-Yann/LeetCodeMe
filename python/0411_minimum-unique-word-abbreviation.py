#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-23 16:13:28
# @Last Modified : 2020-07-23 16:13:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 字符串 "word" 包含以下这些缩写形式： 
# 
#  ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
#  "w1r1", "1o2", "2r1", "3d", "w3", "4"] 
# 
#  给一个目标字符串和一个字符串字典，为目标字符串找一个 最短 长度的缩写字符串，同时这个缩写字符串不是字典中其他字符串的缩写形式。 
# 
#  缩写形式中每一个 数字 或者字母都被视为长度为 1 。比方说，缩写形式 "a32bc" 的长度为 4 而不是 5 。 
# 
#  注意: 
# 
#  
#  如果像第二个示例一样有多个有效答案，你可以返回它们中的任意一个。 
#  假设目标字符串的长度为 m ，字典中的字符串数目为 n 。你可以假设 m ≤ 21， n ≤ 1000， 且 log2(n) + m ≤ 20. 
#  
# 
#  
# 
#  示例: 
# 
#  "apple", ["blade"] -> "a4" (因为 "5" 或者 "4e" 同时也是 "blade" 的缩写形式，所以它们是无效的缩写)
# 
# "apple", ["plain", "amber", "blade"] -> "1p3" (其他有效的缩写形式还包括 "ap3", "a3e", "2p2
# ", "3le", "3l1")。
#  
# 
#  
#  Related Topics 位运算 回溯算法 
#  👍 10 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        """题目啥意思
        对于区分字典中字符串和目标串的话，只要有一个相同位置上的字母不同就可以，保留该位上的字母。
        然后利用整数保存标记j位上不同的字符串是哪些，然后二进制状态压缩枚举保留的位，如果保留的位的tmp或运算为1的个数为n，
        说明保留这些可以覆盖到所有字符串的情况，判断和当前答案的大小即可

        Success: Runtime:156 ms, faster than 100.00% of Python3 online submissions.
         Memory Usage:13.6 MB, less than 100.00% of Python3 online submissions.
        """

        def bits_len(target, bits):
            return sum(((bits >> i) & 1) == 0 for i in range(len(target) - 1))

        diffs = []
        for word in dictionary:
            if len(word) != len(target):
                continue
            diffs.append(sum(2 ** i for i, c in enumerate(word) if target[i] != c))

        if not diffs:
            return str(len(target))

        bits = 2 ** len(target) - 1
        for i in range(2 ** len(target)):
            if all(d & i for d in diffs) and bits_len(target, i) > bits_len(target, bits):
                bits = i

        abbr = []
        pre = 0
        for i in range(len(target)):
            if bits & 1:
                if i - pre > 0:
                    abbr.append(str(i - pre))
                pre = i + 1
                abbr.append(str(target[i]))
            elif i == len(target) - 1:
                abbr.append(str(i - pre + 1))
            bits >>= 1

        return "".join(abbr)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    # [dict(target="apple", dictionary=["blade"]), ["a4"]],
    [dict(target="apple", dictionary=["plain", "amber", "blade"]),
     ["1p3", "ap3", "a3e", "2p2", "3le", "3l1"]],
])
def test_solutions(kw, expected):
    assert Solution().minAbbreviation(**kw) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
