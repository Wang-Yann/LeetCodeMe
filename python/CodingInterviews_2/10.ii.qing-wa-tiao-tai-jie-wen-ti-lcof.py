#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 00:22:30
# @Last Modified : 2020-04-24 00:22:30
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
