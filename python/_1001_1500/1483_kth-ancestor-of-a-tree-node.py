#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0
#  的节点。 
# 
#  请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节
# 点，返回 -1 。 
# 
#  树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
# 
# 输出：
# [null,1,0,-1]
# 
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# 
# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= n <= 5*10^4 
#  parent[0] == -1 表示编号为 0 的节点是根节点。 
#  对于所有的 0 < i < n ，0 <= parent[i] < n 总成立 
#  0 <= node < n 
#  至多查询 5*10^4 次 
#  
#  Related Topics 动态规划

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class TreeAncestor:
    """
    GOOD
    DP倍增法
    状态定义: dp[node][j]，表示 node 的第 2^j 个祖先。其中 node取值为 0~n-1, 列取值为 0~20
    # 题目限定范围 log(50000) < 20
    递推公式: dp[ node ][j] = dp[ dp[node][j-1] ][j-1]

    https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node/solution/dpbei-zeng-fa-dai-ma-qing-xi-python3xiang-xi-zhu-s/
    """

    def __init__(self, n: int, parent: List[int]):
        # log(50000) < 20

        self.cols = 20
        self.dp = [[-1] * self.cols for _ in range(n)]
        for i in range(n):
            self.dp[i][0] = parent[i]
            # 动态规划设置祖先, dp[node][j] 表示 node 往前推第 2^j 个祖先
        for j in range(1, self.cols):
            for i in range(n):
                if self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.cols - 1, -1, -1):
            if k & (1 << i):
                node = self.dp[node][i]
                if node == -1:
                    break

        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])

    assert treeAncestor.getKthAncestor(3, 1) == 1  # // 返回 1 ，它是 3 的父节点
    assert treeAncestor.getKthAncestor(5, 2) == 0  # // 返回 0 ，它是 5 的祖父节点
    assert treeAncestor.getKthAncestor(6, 3) == -1  # // 返回 -1 因为不存在满足要求的祖先节点


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
