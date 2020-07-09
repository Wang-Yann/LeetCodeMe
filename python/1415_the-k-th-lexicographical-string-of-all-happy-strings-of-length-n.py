#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一个 「开心字符串」定义为： 
# 
#  
#  仅包含小写字母 ['a', 'b', 'c']. 
#  对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。 
#  
# 
#  比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字
# 符串。 
# 
#  给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。 
# 
#  请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1, k = 3
# 输出："c"
# 解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
#  
# 
#  示例 2： 
# 
#  输入：n = 1, k = 4
# 输出：""
# 解释：长度为 1 的开心字符串只有 3 个。
#  
# 
#  示例 3： 
# 
#  输入：n = 3, k = 9
# 输出："cab"
# 解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb
# ", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"
#  
# 
#  示例 4： 
# 
#  输入：n = 2, k = 7
# 输出：""
#  
# 
#  示例 5： 
# 
#  输入：n = 10, k = 100
# 输出："abacbabacb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10 
#  1 <= k <= 100 
#  
# 
#  
#  Related Topics 回溯算法

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        nextLetter = {"a": "bc", "b": "ac", "c": "ab"}
        dq = collections.deque(["a", "b", "c"])
        while len(dq):
            if len(dq[0]) == n:
                break
            u = dq.popleft()
            for v in nextLetter[u[-1]]:
                dq.append(u + v)

        return dq[k - 1] if len(dq) >= k else ""


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    """GOOD"""
    def getHappyString(self, n: int, k: int) -> str:
        def generate(prev):
            if len(prev) == n:
                yield prev
                return
            for c in 'abc':
                if not prev or c != prev[-1]:
                    yield from generate(prev + c)

        for i, res in enumerate(generate(''), 1):
            if i == k:
                return res
        return ''


@pytest.mark.parametrize("kw,expected", [
    [dict(n=1, k=3), "c"],
    [dict(n=1, k=4), ""],
    [dict(n=3, k=9), "cab"],
    [dict(n=2, k=7), ""],
    [dict(n=10, k=100), "abacbabacb"],
])
def test_solutions(kw, expected):
    assert Solution().getHappyString(**kw) == expected
    assert Solution1().getHappyString(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
