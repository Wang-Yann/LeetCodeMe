#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-27 21:23:51
# @Last Modified : 2020-04-27 21:23:51
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
from typing import List


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        """
        HARD
        前缀和 单调栈
        我们用数组 P 表示数组 A 的前缀和，即 P[i] = A[0] + A[1] + ... + A[i - 1]。
        我们需要找到 x 和 y，使得 P[y] - P[x] >= K 且 y - x 最小。

        维护一个关于前缀和数组 P 的单调队列，它是一个双端队列（deque），其中存放了下标 x：x0, x1, ... 满足
        P[x0], P[x1], ... 单调递增。这是为了满足性质一。

        当我们遇到了一个新的下标 y 时，我们会在队尾移除若干元素，直到 P[x0], P[x1], ..., P[y] 单调递增。
        这同样是为了满足性质一。

        同时，我们会在队首也移除若干元素，如果 P[y] >= P[x0] + K，则将队首元素移除，直到该不等式不满足。
        这是为了满足性质二。


        https://leetcode-cn.com/problems/shortest-subarray-with-sum-at-least-k/solution/he-zhi-shao-wei-k-de-zui-duan-zi-shu-zu-by-leetcod/
        """
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        # N+1 is impossible
        ans = N + 1
        monoq = collections.deque()
        # Want smallest y-x with Py - Px >= K

        for y, py in enumerate(P):
            # Want opt(y) = largest x with Px <= Py - K
            # 递增
            while monoq and py < P[monoq[-1]]:
                monoq.pop()
            while monoq and py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)
        return ans if ans < N + 1 else -1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(A=[1], K=1),
        dict(A=[1, 2], K=4),
        dict(A=[2, -1, 2], K=3)
    ]
    res = [sol.shortestSubarray(**args) for args in samples]
    print(res)
