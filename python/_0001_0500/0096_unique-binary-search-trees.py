#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 18:13:19
# @Last Modified : 2020-04-20 18:13:19
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
#  示例:
#
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  Related Topics 树 动态规划
#  👍 653 👎 0
import functools

import pytest


class Solution:
    def numTrees(self, n: int) -> int:
        """
        卡塔兰数　　　Cn=(2n)!/(n+1)!n!  
        TODO
        问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：

        G(n) : 长度为n的序列的不同二叉搜索树个数。
        F(i, n): 以i为根的不同二叉搜索树个数(1 <=i  <=n)。

        可见, G(n) 是我们解决问题需要的函数。
        G(n) = ∑ F(i,n)  1<=i<=n
        F(i,n)=G(i−1)⋅G(n−i)
        G(n)= ∑ G(i-1)*G(n-i)    1<=i<=n
        """
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # print(j-1,i-j)
                G[i] += G[j - 1] * G[i - j]
        return G[n]


class Solution1:
    def numTrees(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(idx):
            if idx in (0, 1):
                return 1
            ans = 0
            for i in range(idx):
                ans += dp(i) * dp(idx - 1 - i)
            return ans

        return dp(n)


@pytest.mark.parametrize("args,expected", [
    (3, 5),
    (4, 14),
])
def test_solutions(args, expected):
    assert Solution().numTrees(args) == expected
    assert Solution1().numTrees(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
