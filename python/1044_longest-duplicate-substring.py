#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。 
# 
#  返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。） 
# 
#  
# 
#  示例 1： 
# 
#  输入："banana"
# 输出："ana"
#  
# 
#  示例 2： 
# 
#  输入："abcd"
# 输出：""
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= S.length <= 10^5 
#  S 由小写英文字母组成。 
#  
#  Related Topics 哈希表 二分查找

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestDupSubstring(self, S: str) -> str:
        """
        HARD
        Rabin-Karp
        https://leetcode.com/problems/longest-duplicate-substring/discuss/290871/Python-Binary-Search
        Binary search the length of longest duplicate substring and call the help function test(L).
        test(L) slide a window of length L,
        rolling hash the string in this window,
        record the seen string in a hashset,
        and try to find duplicated string.

        I give it a big mod for rolling hash and it should be enough for this problem.
        """
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 63 - 1

        def test(L):
            """L长度窗口"""
            p = pow(26, L, mod)
            cur = functools.reduce(lambda x, y:(x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            pos = test(mid)
            if pos:
                lo = mid
                res = pos
            else:
                hi = mid - 1
        return S[res:res + lo]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def search(self, L: int, a: int, modulus: int, n: int, nums: List[int]) -> int:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 32

        # binary search, L = repeating string length
        left, right = 1, n
        while left != right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L

        start = self.search(left - 1, a, modulus, n, nums)
        return S[start: start + left - 1] if start != -1 else ""


@pytest.mark.parametrize("args,expected", [
    ("banana", "ana"),
    pytest.param("abcd", ""),
])
def test_solutions(args, expected):
    assert Solution().longestDupSubstring(args) == expected
    assert Solution1().longestDupSubstring(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
