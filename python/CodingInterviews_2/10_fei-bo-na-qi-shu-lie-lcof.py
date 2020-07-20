#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 23:58:10
# @Last Modified : 2020-04-23 23:58:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
#
#  F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
#
#  斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#
#
#  示例 1：
#
#  输入：n = 2
# 输出：1
#
#
#  示例 2：
#
#  输入：n = 5
# 输出：5
#
#
#
#
#  提示：
#
#
#  0 <= n <= 100
#
#
#  注意：本题与主站 509 题相同：https://leetcode-cn.com/problems/fibonacci-number/
#  Related Topics 递归
#  👍 38 👎 0


class Solution:

    def fib(self, n: int) -> int:
        if n in (0, 1):
            return n
        fb = [0] * (n + 1)
        fb[1] = 1
        for i in range(2, n + 1):
            fb[i] = fb[i - 2] + fb[i - 1]
        return fb[n] % 1000000007

    def fib1(self, n: int) -> int:
        if n in (0, 1):
            return n
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = a + b, a
        mod = 1000000007
        return a % mod


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 5, 45
    ]
    res = [sol.fib(args) for args in samples]
    print(res)
