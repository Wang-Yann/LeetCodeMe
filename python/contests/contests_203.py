#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne
# @Created       : 2020-08-22 20:35:06
# @Last Modified : 2020-08-22 20:35:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import bisect
import collections
import functools
import json
from typing import List

import pytest


# 5483
class Solution1:

    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        counter = collections.Counter()
        counter[rounds[0]] = 1
        for s, e in zip(rounds, rounds[1:]):
            if s > e:
                e += n
            for r in range(s + 1, e + 1):
                counter[(r - 1) % n + 1] += 1
        v = max(counter.values())
        # print(counter)
        return sorted([k for k in counter if counter[k] == v])


@pytest.mark.skip
@pytest.mark.parametrize(
    "kwargs,expected", [
        [
            dict(
                n=4, rounds=[
                    1, 3, 1, 2]), [
            1, 2]], [
            dict(
                n=2, rounds=[
                    2, 1, 2, 1, 2, 1, 2, 1, 2]), [2]], [
            dict(
                n=7, rounds=[
                    1, 3, 5, 7]), [
                1, 2, 3, 4, 5, 6, 7]], ])
def test_solutions1(kwargs, expected):
    assert Solution1().mostVisited(**kwargs) == expected


#
# def maxCoins(self, nums: List[int]) -> int:
#     nums = [1] + nums + [1]
#
#     @functools.lru_cache(None)
#     def dp(left, right):
#         if left + 1 == right:
#             return 0
#         return max(
#             nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)
#             for i in range(left + 1, right)
#         )
#
#     return dp(0, len(nums) - 1)

# 5484
class Solution2:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        N = len(piles)
        ans = 0
        for i in range(N // 3):
            piles.pop(0)
            piles.pop()
            ans += piles.pop()
        return ans


@pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [
    [dict(piles=[2, 4, 1, 2, 7, 8]), 9],
    [dict(piles=[2, 4, 5]), 4],
    [dict(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]), 18], ])
def test_solutions2(kwargs, expected):
    assert Solution2().maxCoins(**kwargs) == expected


# 3
class Solution3:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        if m == N:
            return N

        lookup = [0, N + 1]
        for i in range(N - 1, -1, -1):
            t = arr[i]
            idx = bisect.bisect_left(lookup, t)
            bisect.insort_left(lookup, t)
            if m == lookup[idx + 1] - lookup[idx] - 1 or m == lookup[idx] - lookup[idx - 1] - 1:
                return i
        return -1


class Solution31:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        lenToCnt = collections.defaultdict(int)
        iToLen = {}
        res = -1
        for index, x in enumerate(arr):
            # 转成以0为起点的下标
            i = x - 1
            # 原来的左侧和右侧的连续1的长度
            left = 0
            right = 0
            # 新的连续1的起点和终点下标, 初始化为当前下标
            start = i
            end = i
            if i - 1 >= 0 and i - 1 in iToLen:
                # 更新左侧长度和起点下标
                left = iToLen[i - 1]
                start -= left
            if i + 1 < N and i + 1 in iToLen:
                # 更新右侧长度和终点下标
                right = iToLen[i + 1]
                end += right
            newlen = left + right + 1
            # 更新iToLen字典, 只需要更新两个边界即可
            iToLen[start] = newlen
            iToLen[end] = newlen
            # 更新lenToCnt字典, 减去旧长度的值, 加上新长度的值
            lenToCnt[left] -= left
            lenToCnt[right] -= right
            lenToCnt[newlen] += newlen
            # print(iToLen,lenToCnt)

            if lenToCnt[m] > 0:
                # 如果仍有连续1长度为m的部分, 更新最终结果为当前arr下标+1
                res = index + 1
        return res


#
# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [

    [dict(arr=[3, 5, 1, 2, 4], m=1), 4],
    [dict(arr=[3, 1, 5, 4, 2], m=2), -1],
    [dict(arr=[1], m=1), 1],
    [dict(arr=[2, 1], m=2), 2],
    # 大文本直接塞到py文件有问题  TODO
    [dict(arr=json.load(open("./findLatestStepTestcase.json", "rt")), m=75198), -1],

])
def test_solutions3(kwargs, expected):
    assert Solution3().findLatestStep(**kwargs) == expected
    assert Solution31().findLatestStep(**kwargs) == expected


# 4
class Solution4:

    def stoneGameV(self, stoneValue: List[int]) -> int:
        """区间DP"""
        prefix = [0]
        N = len(stoneValue)
        for t in stoneValue:
            prefix.append(prefix[-1] + t)

        # print(prefix)

        @functools.lru_cache(None)
        def dp(start=0, end=N - 1):
            if end == start:
                return 0

            ret = 0
            for mid in range(start + 1, end + 1):
                # l : start : mid-1
                # r : mid   : end
                sum_l = prefix[mid] - prefix[start]
                sum_r = prefix[end + 1] - prefix[mid]
                if sum_l <= sum_r:
                    ret = max(ret, sum_l + dp(start, mid - 1))
                if sum_r <= sum_l:
                    ret = max(ret, sum_r + dp(mid, end))
            return ret

        return dp(0, N - 1)


# @pytest.mark.skip
@pytest.mark.parametrize("kwargs,expected", [[dict(stoneValue=[6, 2, 3, 4, 5, 5]), 18], [
    dict(stoneValue=[7, 7, 7, 7, 7, 7, 7]), 28], [dict(stoneValue=[4]), 0], ])
def test_solutions4(kwargs, expected):
    assert Solution4().stoneGameV(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
