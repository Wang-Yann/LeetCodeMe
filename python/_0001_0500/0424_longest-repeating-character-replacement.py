#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。
#  
# 
#  注意: 
# 字符串长度 和 k 不会超过 104。 
# 
#  示例 1: 
# 
#  输入:
# s = "ABAB", k = 2
# 
# 输出:
# 4
# 
# 解释:
# 用两个'A'替换为两个'B',反之亦然。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "AABABBA", k = 1
# 
# 输出:
# 4
# 
# 解释:
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#  
#  Related Topics 双指针 Sliding Window

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        counter = collections.defaultdict(int)
        ans = 0
        right = 0
        max_freq = 0
        for left in range(N):
            while right < N and right - left - max_freq <= k:
                counter[s[right]] += 1
                max_freq = max(max_freq, counter[s[right]])
                right += 1
            # update ans
            if right - left - max_freq > k:
                ans = max(ans, right - 1 - left)
            else:
                ans = max(ans, right - left)

            # update max_freq
            counter[s[left]] -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        N = len(s)
        max_n = left = right = 0

        while right < N:
            num[ord(s[right]) - ord("A")] += 1
            max_n = max(max_n, num[ord(s[right]) - ord("A")])
            if right - left + 1 - max_n > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="ABAB", k=2), 4),
    pytest.param(dict(s="AABABBA", k=1), 4),
])
@pytest.mark.parametrize("SolutionCLS", [Solution,Solution])
def test_solutions(kwargs, expected,SolutionCLS):
    assert SolutionCLS().characterReplacement(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
