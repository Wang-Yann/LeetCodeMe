#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 18:40:53
# @Last Modified : 2020-08-08 18:40:53
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，一个分割被称为 「好分割」 当它满足：将 s 分割成 2 个字符串 p 和 q ，它们连接起来等于 s 且 p 和 q 中不同字符的数
# 目相同。 
# 
#  请你返回 s 中好分割的数目。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "aacaba"
# 输出：2
# 解释：总共有 5 种分割字符串 "aacaba" 的方法，其中 2 种是好分割。
# ("a", "acaba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
# ("aa", "caba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
# ("aac", "aba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
# ("aaca", "ba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
# ("aacab", "a") 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。
#  
# 
#  示例 2： 
# 
#  输入：s = "abcd"
# 输出：1
# 解释：好分割为将字符串分割成 ("ab", "cd") 。
#  
# 
#  示例 3： 
# 
#  输入：s = "aaaaa"
# 输出：4
# 解释：所有分割都是好分割。 
# 
#  示例 4： 
# 
#  输入：s = "acbadbaada"
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  s 只包含小写英文字母。 
#  1 <= s.length <= 10^5 
#  
#  Related Topics 位运算 字符串 
#  👍 2 👎 0
	 

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numSplits(self, s: str) -> int:
        """AC 仔细读题"""
        counter = collections.Counter(s)
        cnt = len(counter)
        window = set()
        ans = 0
        i = 0
        N = len(s)
        while i < N:
            while i < N and len(window) < cnt // 2:
                window.add(s[i])
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    counter.pop(s[i])
                i += 1
            if len(window) == len(counter):
                ans += 1
            # print(window, counter)
            window.add(s[i])
            counter[s[i]] -= 1
            if counter[s[i]] == 0:
                counter.pop(s[i])
            i += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):

    def numSplits(self, s):
        left_count, right_count = collections.Counter(), collections.Counter(s)
        result = 0
        for c in s:
            left_count[c] += 1
            right_count[c] -= 1
            if not right_count[c]:
                del right_count[c]
            if len(left_count) == len(right_count):
                result += 1
        return result


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="aacaba"), 2],

    pytest.param(dict(s="abcd"), 1),
    pytest.param(dict(s="aaaaa"), 4),
    pytest.param(dict(s="acbadbaada"), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().numSplits(**kwargs) == expected
    assert Solution1().numSplits(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
