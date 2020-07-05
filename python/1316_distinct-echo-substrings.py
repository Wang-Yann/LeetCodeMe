#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 19:57:14
# @Last Modified : 2020-07-05 19:57:14
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个字符串 text ，请你返回满足下述条件的 不同 非空子字符串的数目： 
# 
#  
#  可以写成某个字符串与其自身相连接的形式（即，可以写为 a + a，其中 a 是某个字符串）。 
#  
# 
#  例如，abcabc 就是 abc 和它自身连接形成的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：text = "abcabcabc"
# 输出：3
# 解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。
#  
# 
#  示例 2： 
# 
#  输入：text = "leetcodeleetcode"
# 输出：2
# 解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 2000 
#  text 只包含小写英文字母。 
#  
#  Related Topics 字符串 
#  👍 21 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def distinctEchoSubstrings(self, text: str) -> int:
        """啥题意"""
        N = len(text)
        seen = set()
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if j * 2 - i <= N and text[i:j] == text[j:j * 2 - i] and text[i:j] not in seen:
                    ans += 1
                    # print(text[i:j])
                    seen.add(text[i:j])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def distinctEchoSubstrings(self, text: str) -> int:
        """
        Rabin-Karp 算法 ，其核心是将字符串看成一个 k 进制的整数，其中 k 是字符串中可能出现的字符种类
        """
        N = len(text)

        MOD, BASE = 10 ** 9 + 7, 31
        pre, mul = [0] * (N + 1), [1] + [0] * N
        for i in range(1, N + 1):
            pre[i] = (pre[i - 1] * BASE + ord(text[i - 1])) % MOD
            mul[i] = mul[i - 1] * BASE % MOD

        def get_hash(l, r):
            return (pre[r + 1] - pre[l] * mul[r - l + 1] % MOD + MOD) % MOD

        seen = {x:set() for x in range(N)}
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                l = j - i
                if j + l <= N:
                    hash_left = get_hash(i, j - 1)
                    # """ 需要牢记在实际应用中，这样做是不严谨的
                    # 需要 先判断两个实例的哈希值是否相等，再判断它们本质上是否相等"""
                    if hash_left not in seen[l - 1] and hash_left == get_hash(j, j + l - 1):
                        ans += 1
                        seen[l - 1].add(hash_left)
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(text="abcabcabc"), 3),
    pytest.param(dict(text="leetcodeleetcode"), 2),
])
def test_solutions(kwargs, expected):
    assert Solution().distinctEchoSubstrings(**kwargs) == expected
    assert Solution1().distinctEchoSubstrings(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
