#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-27 11:58:03
# @Last Modified : 2020-04-27 11:58:03
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List


class Solution0:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        方法 2：维护最小值栈
        对于每个 j，考虑所有子序列 [i, j] 的最小值。想法是每当我们增加 j，这些最小值可能会有关联，事实上，
        min(A[i:j+1]) = min(A[i:j], A[j+1])。
        https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/zi-shu-zu-de-zui-xiao-zhi-zhi-he-by-leetcode/
        """
        ans = 0
        stack = []
        MOD = 10 ** 9 + 7
        dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, cnt = stack.pop()
                count += cnt
                dot -= x * cnt
            stack.append((y, count))
            dot += y * count
            ans += dot

        return ans % MOD


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        TODO GOOD
        双单调栈
        计算以当前位置元素i为最小值的子数组个数k. res += i*k。
        其中:k=(左边连续小于等于当前值的数组长度+1)*(右边连续小于当前值的数组长度+1)
        """
        MOD = 10 ** 9 + 7
        length = len(A)
        left, s1 = [0] * length, []
        for i in range(length):
            ##递增
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append((A[i], count))
        right, s2 = [0] * length, []
        for i in range(length - 1, -1, -1):
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append((A[i], count))
        # print(A, left, right)

        return sum(a * l * r for a, l, r in zip(A, left, right)) % MOD


if __name__ == '__main__':
    sol = Solution()
    samples = [
        # [3, 1, 2, 4],
        [3, 1, 5, 3, 1, 2, 4],
        # [],
        # [1]

    ]
    lists = [x for x in samples]
    res = [sol.sumSubarrayMins(x) for x in lists]
    print(res)
