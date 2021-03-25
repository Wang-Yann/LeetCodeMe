#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-04 23:28:32
# @Last Modified : 2020-07-04 23:28:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。 
# 
#  假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。 
# 
#  
# 
#  给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。 
# 
#  你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。 
# 
#  请返回待替换子串的最小可能长度。 
# 
#  如果原字符串自身就是一个平衡字符串，则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "QWER"
# 输出：0
# 解释：s 已经是平衡的了。 
# 
#  示例 2： 
# 
#  输入：s = "QQWE"
# 输出：1
# 解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
#  
# 
#  示例 3： 
# 
#  输入：s = "QQQW"
# 输出：2
# 解释：我们可以把前面的 "QQ" 替换成 "ER"。 
#  
# 
#  示例 4： 
# 
#  输入：s = "QQQQ"
# 输出：3
# 解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s.length 是 4 的倍数 
#  s 中只含有 'Q', 'W', 'E', 'R' 四种字符 
#  
#  Related Topics 双指针 字符串 
#  👍 31 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def balancedString(self, s: str) -> int:
        counter = collections.Counter(s)
        res = N = len(s)
        l = 0
        for r, char in enumerate(s):
            counter[char] -= 1
            while l < N and all(N // 4 >= counter[c] for c in "QWER"):
                res = min(res, r - l + 1)
                counter[s[l]] += 1
                l += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        s="QWER"
    ), 0),
    pytest.param(dict(s="QQWE"), 1),
    pytest.param(dict(s="QQQW"), 2),
    pytest.param(dict(s="QQQQ"), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().balancedString(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
