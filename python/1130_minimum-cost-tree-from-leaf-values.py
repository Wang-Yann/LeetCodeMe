#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

r"""
# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树： 
# 
#  
#  每个节点都有 0 个或是 2 个子节点。 
#  数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。） 
#  每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。 
#  
# 
#  在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。 
# 
#  
# 
#  示例： 
# 
#  输入：arr = [6,2,4]
# 输出：32
# 解释：
# 有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。
# 
#     24            24
#    /  \          /  \
#   12   4        6    8
#  /  \               / \
# 6    2             2   4 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 40 
#  1 <= arr[i] <= 15 
#  答案保证是一个 32 位带符号整数，即小于 2^31。 
#  
#  Related Topics 栈 树 动态规划
"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        """
        区间DP
        https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/solution/dong-tai-gui-hua-dan-diao-zhan-python3-by-smoon1-2/
        """
        N = len(arr)
        dp = [[0x7fffffff for _ in range(N)] for _ in range(N)]
        maxval = [[0 for _ in range(N)] for _ in range(N)]
        # 求区间[i, j]中最大元素
        for i in range(N):
            for j in range(i, N):
                maxval[i][j] = max(arr[i:j + 1])
        # 叶子结点不参与计算
        for i in range(N):
            dp[i][i] = 0
        # 枚举区间长度
        for l in range(1, N):
            # 枚举区间起始点
            for start in range(N - l):
                # 枚举划分两棵子树
                for k in range(start, start + l):
                    dp[start][start + l] = min(
                        dp[start][start + l],
                        dp[start][k] + dp[k + 1][start + l] + maxval[start][k] * maxval[k + 1][start + l]
                    )
        # print(dp, maxval)
        return dp[0][N - 1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def mctFromLeafValues(self, A: List[int]) -> int:
        """ 单调栈
        维护一个单调递减栈，每次用相邻的两个较小的叶节点合成中间节点，最终可以得到最小代价生成树

        """
        res, N = 0, len(A)
        stack = [0x7fffffff]
        for a in A:
            # print(stack)
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        # print(stack)
        return res


@pytest.mark.parametrize("args,expected", [
    ([6, 2, 4], 32)
])
def test_solutions(args, expected):
    assert Solution().mctFromLeafValues(args) == expected
    assert Solution1().mctFromLeafValues(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
