#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，它只包含三种字符 a, b 和 c 。 
# 
#  请你返回 a，b 和 c 都 至少 出现过一次的子字符串数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcabc"
# 输出：10
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bc
# abc", "cab", "cabc" 和 "abc" (相同字符串算多次)。
#  
# 
#  示例 2： 
# 
#  输入：s = "aaacb"
# 输出：3
# 解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。
#  
# 
#  示例 3： 
# 
#  输入：s = "abc"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= s.length <= 5 x 10^4 
#  s 只包含字符 a，b 和 c 。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        滑动窗口
        可以观察到一个性质：从下标 i 开始的所有子串，我们按顺序从前到后考虑，一定是前部分均非法，后部分均合法 ，
        简单来说，假设 [i,j]  的子串已经合法，那么 [i,j+1]  必然合法，如果 [i,j]  非法，那么 [i,j-1] 必然非法，这是很显然的

        """
        ans = i = 0
        window = dict.fromkeys("abc", 0)
        for r, char in enumerate(s):
            window[char] += 1
            while all(window.values()):
                window[s[i]] -= 1
                i += 1
            # print(r,i,window)
            ans += i
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        """
        GOOD
        last will record the position of last occurrence.
        If the ending index of substring is i,
        the starting position should be on the left of min(last),
        in order to have all 3 different letters.
        And in this case, the starting index can be in range [0, min(last)],
        min(last) + 1 in total.
        """
        res, last = 0, [-1] * 3
        for i, c in enumerate(s):
            last[ord(c) - 97] = i
            res += 1 + min(last)
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abcabc"), 10],
    # [dict(s="aaacb"), 3],
    # [dict(s="abc"), 1],
])
def test_solutions(kw, expected):
    assert Solution().numberOfSubstrings(**kw) == expected
    assert Solution1().numberOfSubstrings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
