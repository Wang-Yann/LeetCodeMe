#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 16:09:28
# @Last Modified : 2020-08-04 16:09:28
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 S，找出所有长度为 K 且不含重复字符的子串，请你返回全部满足要求的子串的 数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "havefunonleetcode", K = 5
# 输出：6
# 解释：
# 这里有 6 个满足题意的子串，分别是：'havef','avefu','vefun','efuno','etcod','tcode'。
#  
# 
#  示例 2： 
# 
#  输入：S = "home", K = 5
# 输出：0
# 解释：
# 注意：K 可能会大于 S 的长度。在这种情况下，就无法找到任何长度为 K 的子串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 10^4 
#  S 中的所有字符均为小写英文字母 
#  1 <= K <= 10^4 
#  
#  Related Topics 字符串 Sliding Window 
#  👍 13 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        """AC"""
        N = len(S)
        if N < K:
            return 0
        ans = 0
        window = []
        for r in range(N):
            r_char = S[r]
            window.append(r_char)
            while len(window) != len(set(window)) or len(window) > K:
                window.pop(0)
            if len(window) == K:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def numKLenSubstrNoRepeats(self, S, K):

        result, i = 0, 0
        lookup = set()
        for r in range(len(S)):
            while S[r] in lookup:
                lookup.remove(S[i])
                i += 1
            lookup.add(S[r])
            result += r - i + 1 >= K
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(S="havefunonleetcode", K=5), 6],
    [dict(S="home", K=5), 0],
])
def test_solutions(kw, expected):
    assert Solution().numKLenSubstrNoRepeats(**kw) == expected
    assert Solution1().numKLenSubstrNoRepeats(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
