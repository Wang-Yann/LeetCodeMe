#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 15:00:24
# @Last Modified : 2020-08-09 15:00:24
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import functools
import math
import operator
from typing import List

import pytest


# 5483
class Solution1:

    def makeGood(self, s: str) -> str:
        chars = list(s)
        need_change = True
        while need_change:
            new_chars = []
            i = 0
            need_change = False
            while i < len(chars):
                if i + 1 < len(chars) and chars[i].lower() == chars[i + 1].lower() and chars[i] != chars[i + 1]:
                    i += 2
                    need_change = True
                else:
                    new_chars.append(chars[i])
                    i += 1
            chars = new_chars
        return "".join(chars)


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="leEeetcode"), "leetcode"],
    pytest.param(dict(s="abBAcC"), ""),
    pytest.param(dict(s="s"), "s"),
    pytest.param(dict(s=""), ""),
    pytest.param(dict(s="Ss"), ""),
])
def test_solutions1(kwargs, expected):
    assert Solution1().makeGood(**kwargs) == expected


# 5484
class Solution2:

    def findKthBit(self, n: int, k: int) -> str:
        hash_map = {"0": "1", "1": "0"}
        s = ["0"]
        for i in range(n - 1):
            rs = [hash_map[b] for b in s][::-1]
            s = s + ["1"] + rs
        # print(s)
        return s[k - 1]


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=3, k=1), "0"],
    pytest.param(dict(n=4, k=11), "1"),
    pytest.param(dict(n=1, k=1), "0"),
    pytest.param(dict(n=2, k=3), "1"),
])
def test_solutions2(kwargs, expected):
    assert Solution2().findKthBit(**kwargs) == expected


# 3
class Solution3:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        """target=0到 情况"""
        prefix = {0: -1}
        accu = 0
        segs = []
        for r, v in enumerate(nums):
            accu += v
            if target != 0:
                prefix[accu] = r
                if accu - target in prefix:
                    l = prefix[accu - target]
                    segs.append([l, r])
            else:
                if accu - target in prefix:
                    l = prefix[accu - target]
                    segs.append([l, r])
                prefix[accu] = r

        # print(segs)
        # 贪心选取
        segs.sort()
        N = len(segs)
        need_remove = 0
        end = float("-inf")
        for interval in sorted(segs, key=operator.itemgetter(1)):
            if interval[0] >= end:
                end = interval[1]
            else:
                need_remove += 1
        return N - need_remove

    # 435
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        end = float("-inf")
        for interval in sorted(intervals, key=operator.itemgetter(1)):
            if interval[0] >= end:
                end = interval[1]
            else:
                ans += 1
        return ans


#
@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[1, 1, 1, 1, 1], target=2), 2],

    pytest.param(dict(nums=[-1, 3, 5, 1, 4, 2, -9], target=6), 2),
    pytest.param(dict(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10), 3),
    pytest.param(dict(nums=[0, 0, 0], target=0), 3),
    pytest.param(dict(
        nums=[0, 0, -1, 0, -2, 0, 1, 0, 1, -2, -1, 2, 2, 1, -2, -2, -1, 0, 2, 2, -2, 2, 2, 0, 2, 0, -1, 1, 1, 1, 2, 1, 2, -2, -2, 0, 1, 1, 0, 2, 0, 1,
              0, 1, 2, 2, 1, 0, -1, 0, 1, 0, 2, 1, -1, 2, -2, 2, -2, 1, -1, 0, 2, -2, 0, 1, 1, -1, 1, 2, -2, -1, -2, 0, 2, -2, 0, 2, -1, -2, -1, 2,
              -1, -2, -1, 2, 1, 1, 0, 2, -1, 2, 1, -2, 0, 0, -1, 1, 1, -1, 0, -2, 1, -1, 0, -1, 2, 1, 1, 1, 2, -1, 1, 1, 0, 1, 1, 0, 0, -1, -1, 0, 0,
              -1, 2, -2, 0, 1, 1, 2, -1, 1, 1, 0, 0, -2, 0, -1, -2, 1],
        target=0), 54),
])
def test_solutions3(kwargs, expected):
    assert Solution3().maxNonOverlapping(**kwargs) == expected


# 4
class Solution4:

    def minCost(self, n: int, cuts: List[int]) -> int:
        """结束后AC"""
        cuts=[0]+cuts+[n]
        cuts.sort()

        @functools.lru_cache(None)
        def dp(l, r):
            if   l >= r - 1:
                return 0
            ans = math.inf
            for k in range(l+1,r):
                new_v = dp(l, k) + dp(k, r) + cuts[r] - cuts[l]
                ans = min(ans, new_v)
            return ans if ans != math.inf else 0

        return dp(0, len(cuts)-1)


# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(n=7, cuts=[1, 3, 4, 5]), 16],

    # 注意 竟然粘贴错用例答案了 ！！！！ 25
    pytest.param(dict(n=9, cuts=[5, 6, 1, 4, 2]), 22),
])
def test_solutions4(kwargs, expected):
    assert Solution4().minCost(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
