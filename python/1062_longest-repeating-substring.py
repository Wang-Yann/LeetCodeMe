#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-03 11:53:18
# @Last Modified : 2020-08-03 11:53:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定字符串 S，找出最长重复子串的长度。如果不存在重复子串就返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abcd"
# 输出：0
# 解释：没有重复子串。
#  
# 
#  示例 2： 
# 
#  输入："abbaba"
# 输出：2
# 解释：最长的重复子串为 "ab" 和 "ba"，每个出现 2 次。
#  
# 
#  示例 3： 
# 
#  输入："aabcaabdaab"
# 输出：3
# 解释：最长的重复子串为 "aab"，出现 3 次。
#  
# 
#  示例 4： 
# 
#  输入："aaaaa"
# 输出：4
# 解释：最长的重复子串为 "aaaa"，出现 2 次。 
# 
#  
# 
#  提示： 
# 
#  
#  字符串 S 仅包含从 'a' 到 'z' 的小写英文字母。 
#  1 <= S.length <= 1500 
#  
#  Related Topics 字符串 
#  👍 22 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestRepeatingSubstring(self, S: str) -> int:

        def search(L: int) -> int:
            """
            Search a substring of given length
            that occurs at least 2 times.
            @return start position if the substring exits and -1 otherwise.
            """
            seen = set()
            for start in range(0, N - L + 1):
                tmp = S[start:start + L]
                if tmp in seen:
                    return start
                # 使用hash方式
                # h = hash(tmp)
                # if h in seen:
                #     return start
                # seen.add(h)
                seen.add(tmp)
            return -1

        N = len(S)
        l, r = 1, N
        while l <= r:
            L = (l + r) >> 1
            if search(L) != -1:
                l = L + 1
            else:
                r = L - 1
        return l - 1


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:

    def longestRepeatingSubstring(self, S: str) -> str:
        N = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(N)]
        # base value for the rolling hash function
        A = 26
        # modulus value for the rolling hash function to avoid overflow
        # 2**24 (无符号整型数的最大值）是足够的
        MOD = 2 ** 24

        def search(L: int) -> int:
            """
            Rabin-Karp with polynomial rolling hash.
            Search a substring of given length
            that occurs at least 2 times.
            @return start position if the substring exits and -1 otherwise.
            """
            # compute the hash of string S[:L]
            h = 0
            for i in range(L):
                h = (h * A + nums[i]) % MOD

            # already seen hashes of strings of length L
            seen = {h}
            # const value to be used often : a**L % modulus
            aL = pow(A, L, MOD)
            for start in range(1, N - L + 1):
                # compute rolling hash in O(1) time
                h = (h * A - nums[start - 1] * aL + nums[start + L - 1]) % MOD
                if h in seen:
                    return start
                seen.add(h)
            return -1

        # binary search, L = repeating string length
        l, r = 1, N
        while l <= r:
            L = (l + r) >> 1
            if search(L) != -1:
                l = L + 1
            else:
                r = L - 1

        return l - 1


@pytest.mark.parametrize("args,expected", [
    ("abcd", 0),
    ("abbaba", 2),
    ("aabcaabdaab", 3),
    ("aaaaa", 4),
])
def test_solutions(args, expected):
    assert Solution().longestRepeatingSubstring(args) == expected
    assert Solution1().longestRepeatingSubstring(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
