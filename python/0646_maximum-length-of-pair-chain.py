#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 22:50:53
# @Last Modified : 2020-04-29 22:50:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """ 使用贪心思想扩展数对链，在所有可作为下一个数对的集合中选择第二个数最小的数对添加到数对链"""
        pairs.sort(key=lambda x:x[1])
        cnt, i = 0, 0
        for j in range(len(pairs)):
            if j == 0 or pairs[i][1] < pairs[j][0]:
                cnt += 1
                i = j
        return cnt


class Solution1:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        dp[i] 存储以 pairs[i] 结尾的最长链的长度。当 i < j 且 pairs[i][1] < pairs[j][0] 时，扩展数对链，更新 dp[j] = max(dp[j], dp[i] + 1)。

        """
        pairs.sort()
        dp = [1] * len(pairs)
        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)


@pytest.mark.parametrize("args,expected", [
    ([[1, 2], [2, 3], [3, 4]], 2),
    ([[1,2]], 1)
])
def test_solutions(args, expected):
    assert Solution().findLongestChain(args) == expected
    assert Solution1().findLongestChain(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
