#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 12:55:53
# @Last Modified : 2020-04-11 12:55:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



"""
# 你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N 共有 N 层楼的建筑。
#
#  每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
#
#  你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
#
#  每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
#
#  你的目标是确切地知道 F 的值是多少。
#
#  无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？
#
#
#
#
#
#
#  示例 1：
#
#  输入：K = 1, N = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
# 如果它没碎，那么我们肯定知道 F = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
#
#
#  示例 2：
#
#  输入：K = 2, N = 6
# 输出：3
#
#
#  示例 3：
#
#  输入：K = 3, N = 14
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= K <= 100
#  1 <= N <= 10000
#
#  Related Topics 数学 二分查找 动态规划
#  👍 435 👎 0

"""

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
