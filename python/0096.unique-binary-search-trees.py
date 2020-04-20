#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 18:13:19
# @Last Modified : 2020-04-20 18:13:19
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class Solution:
    def numTrees(self, n: int) -> int:
        """
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
                G[i] += G[j - 1] * G[i - j]
        return G[n]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        3, 4

    ]
    lists = [x for x in samples]
    res = [sol.numTrees(x) for x in lists]
    print(res)
