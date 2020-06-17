#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串数组 A，找到以 A 中每个字符串作为子字符串的最短字符串。 
# 
#  我们可以假设 A 中没有字符串是 A 中另一个字符串的子字符串。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["alex","loves","leetcode"]
# 输出："alexlovesleetcode"
# 解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。 
# 
#  示例 2： 
# 
#  输入：["catg","ctaagt","gcta","ttca","atgcatc"]
# 输出："gctaagttcatgcatc" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 12 
#  1 <= A[i].length <= 20 
#  
# 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        """
        官方题解
        状压DP
        """
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in range(1 << N)]
        parent = [[None] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1 << N) - 1
        # 最后一行值最大的index
        i = max(range(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i - 1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (["alex", "loves", "leetcode"], "alexlovesleetcode"),
    (["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "gctaagttcatgcatc"),
])
def test_solutions(args, expected):
    assert Solution().shortestSuperstring(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
