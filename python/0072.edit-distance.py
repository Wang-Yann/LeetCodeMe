#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 21:47:05
# @Last Modified : 2020-04-06 21:47:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

class Solution:
    """我们用 D[i][j] 表示 A 的前 i 个字母和 B 的前 j 个字母之间的编辑距离。"""
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # 有一个字符串为空串
        if n * m == 0:
            return n + m

        # DP 数组
        D = [[0] * (m + 1) for _ in range(n + 1)]

        # 边界状态初始化
        for i in range(n + 1):
            D[i][0] = i
        for j in range(m + 1):
            D[0][j] = j

        # 计算所有 DP 值

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                delete = D[i - 1][j] + 1
                insert = D[i][j - 1] + 1
                replace = D[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                D[i][j] = min(insert, delete, replace)

        return D[n][m]

if __name__ == '__main__':
    sol = Solution()
    sample="abcd"
    sample1="aed"
    print(sol.minDistance(sample,sample1))
