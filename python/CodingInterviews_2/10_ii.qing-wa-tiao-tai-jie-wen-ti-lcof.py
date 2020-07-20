#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 00:22:30
# @Last Modified : 2020-04-24 00:22:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
#
#  答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
#  示例 1：
#
#  输入：n = 2
# 输出：2
#
#
#  示例 2：
#
#  输入：n = 7
# 输出：21
#
#
#  提示：
#
#
#  0 <= n <= 100
#
#
#  注意：本题与主站 70 题相同：https://leetcode-cn.com/problems/climbing-stairs/
#
#
#  Related Topics 递归
#  👍 47 👎 0

class Solution:

    def numWays(self, n: int) -> int:
        fb = [1, 1, 2]
        for i in range(3, n + 1):
            fb.append(fb[i - 2] + fb[i - 1])
        return fb[n] % 1000000007


if __name__ == '__main__':
    sol = Solution()
    samples = [
        2, 7
    ]
    res = [sol.numWays(args) for args in samples]
    print(res)
