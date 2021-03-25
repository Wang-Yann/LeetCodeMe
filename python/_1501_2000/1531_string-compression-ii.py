#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 14:03:40
# @Last Modified : 2020-08-09 14:03:40
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "
# aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。 
# 
#  注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。 
# 
#  给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。 
# 
#  请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aaabcccd", k = 2
# 输出：4
# 解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3
# c3" ，长度是 4 。 
# 
#  示例 2： 
# 
#  输入：s = "aabbaa", k = 2
# 输出：2
# 解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
#  
# 
#  示例 3： 
# 
#  输入：s = "aaaaaaaaaaa", k = 0
# 输出：3
# 解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  0 <= k <= s.length 
#  s 仅包含小写英文字母 
#  
#  Related Topics 字符串 动态规划 
#  👍 25 👎 0
	 

"""

import functools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """GOOD"""
        def compress(ch, cnt):
            if cnt == 0:
                return ''
            if cnt == 1:
                return ch
            return '%s%d' % (ch, cnt)

        N = len(s)

        @functools.lru_cache(None)
        def dp(i, pre_char, pre_cnt, k):
            if i == N:
                return len(compress(pre_char, pre_cnt))

            candidates = []
            if k > 0:
                candidates.append(dp(i + 1, pre_char, pre_cnt, k - 1))  # if delete s[i]

            # if keep s[i]
            if s[i] == pre_char:
                candidates.append(dp(i + 1, pre_char, pre_cnt + 1, k))
            else:
                candidates.append(dp(i + 1, s[i], 1, k) + len(compress(pre_char, pre_cnt)))
            # print(i,pre_char,pre_cnt,k,candidates)
            return min(candidates)

        return dp(0, '', 0, k)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="aaabcccd", k=2), 4],

    # pytest.param(dict(s="aabbaa", k=2), 2),
    # pytest.param(dict(s="aaaaaaaaaaa", k=0), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().getLengthOfOptimalCompression(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
