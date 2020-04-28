#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 12:55:53
# @Last Modified : 2020-04-11 12:55:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        def check(n, K, N):
            # Each combination of n moves with k broken eggs could represent a unique F.
            # Thus, the range size of F that all cominations can cover
            # is the sum of C(n, k), k = 1..K
            total, c = 0, 1
            for k in range(1, K + 1):
                c *= n - k + 1
                c //= k
                total += c
                if total >= N:
                    return True
            return False

        left, right = 1, N
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid, K, N):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def superEggDropS(self, K: int, N: int) -> int:
        """ 需要掌握
        方法一：动态规划 + 二分搜索
        状态可以表示成 (K, N)( ，其中 K为鸡蛋数，N 为楼层数
        我们定义 dp(K, N)  为在状态 (K, N) 下最少需要的步数

        如果鸡蛋不碎，那么状态变成 (K, N-X) ，即我们鸡蛋的数目不变，但答案只可能在上方的 N-X  层楼了。
        也就是说，我们把原问题缩小成了一个规模为 (K, N-X) 的子问题；

        如果鸡蛋碎了，那么状态变成 (K-1, X-1)( ，即我们少了一个鸡蛋，但我们知道答案只可能在第 XX 楼下方的 X-1  层楼中了。
        也就是说，我们把原问题缩小成了一个规模为 (K-1, X-1)  的子问题。

        """
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) // 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x
                    print([k,n],lo,hi)
                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)


if __name__ == '__main__':
    sol = Solution()
    sample = []
    K = 10
    N = 60
    # K = 1
    # N = 2
    # K = 3
    # N = 1
    # K = 1
    # N = 1
    # K = 1
    # N = 4
    print(sol.superEggDropS(K, N))
