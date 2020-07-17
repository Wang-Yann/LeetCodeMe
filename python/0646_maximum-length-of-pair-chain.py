#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 22:50:53
# @Last Modified : 2020-04-29 22:50:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。
#
#  现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。
#
#  给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。
#
#  示例 :
#
#
# 输入: [[1,2], [2,3], [3,4]]
# 输出: 2
# 解释: 最长的数对链是 [1,2] -> [3,4]
#
#
#  注意：
#
#
#  给出数对的个数在 [1, 1000] 范围内。
#
#  Related Topics 动态规划
#  👍 100 👎 0

"""

from typing import List

import pytest


class Solution:

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """ 使用贪心思想扩展数对链，在所有可作为下一个数对的集合中选择第二个数最小的数对添加到数对链"""
        pairs.sort(key=lambda x: x[1])
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
    ([[1, 2]], 1)
])
def test_solutions(args, expected):
    assert Solution().findLongestChain(args) == expected
    assert Solution1().findLongestChain(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
