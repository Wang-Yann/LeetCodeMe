#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 22:58:23
# @Last Modified : 2021-02-22 22:58:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 小扣参加的秋日市集景区共有 $N$ 个景点，景点编号为 $1$~$N$。景点内设有 $N-1$ 条双向道路，使所有景点形成了一个二叉树结构，根结点记为 `r
# oot`，景点编号即为节点值。
# 
# 由于秋日市集景区的结构特殊，游客很容易迷路，主办方决定在景区的若干个景点设置导航装置，按照所在景点编号升序排列后定义装置编号为 1 ~ M。导航装置向游客发
# 送数据，数据内容为列表 `[游客与装置 1 的相对距离,游客与装置 2 的相对距离,...,游客与装置 M 的相对距离]`。由于游客根据导航装置发送的信息来确认
# 位置，因此主办方需保证游客在每个景点接收的数据信息皆不相同。请返回主办方最少需要设置多少个导航装置。
# 
# **示例 1：**
# >输入：`root = [1,2,null,3,4]`
# >
# >输出：`2`
# >
# >解释：在景点 1、3 或景点 1、4 或景点 3、4 设置导航装置。
# >
# >![image.png](https://pic.leetcode-cn.com/1597996812-tqrgwu-image.png){:height
# ="250px"}
# 
# 
# 
# **示例 2：**
# >输入：`root = [1,2,3,4]`
# >
# >输出：`1`
# >
# >解释：在景点 3、4 设置导航装置皆可。
# >
# >![image.png](https://pic.leetcode-cn.com/1597996826-EUQRyz-image.png){:height
# ="200px"}
# 
# 
# 
# **提示：**
# - `2 <= N <= 50000`
# - 二叉树的非空节点值为 `1~N` 的一个排列。
#  👍 6 👎 0
  

"""
import functools

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def navigation(self, root: TreeNode) -> int:
        """
        https://leetcode-cn.com/problems/hSRGyL/solution/python-shen-qi-de-ji-yi-hua-sou-suo-by-zerotrac2/
        dp(node, inside, outside) 表示对于以 node 为根节点的子树
        子树内部的摄像头情况为 inside（True 为必须有，False 为可以有）
        子树外部的摄像头情况为 outside（同上）
        需要的摄像头个数
    """

        @functools.lru_cache(None)
        def dfs(node: TreeNode, inside: bool, outside: bool) -> int:
            # 叶节点
            if not node.left and not node.right:
                return int(inside)
            # 只有右孩子
            if not node.left:
                return min(
                    1 + dfs(node.right, False, True),
                    dfs(node.right, inside, outside)
                )
            # 只有左孩子
            if not node.right:
                return min(
                    1 + dfs(node.left, False, True),
                    dfs(node.left, inside, outside)
                )
            # 根节点
            if node == root:
                return min(
                    1 + dfs(node.left, True, True) + dfs(node.right, False, True),
                    1 + dfs(node.left, False, True) + dfs(node.right, True, True),
                    dfs(node.left, True, False) + dfs(node.right, False, True),
                    dfs(node.left, False, True) + dfs(node.right, True, False),
                    dfs(node.left, True, True) + dfs(node.right, True, True)
                )
            # 一般情况
            if outside:
                return min(
                    dfs(node.left, True, outside) + dfs(node.right, False, True),
                    dfs(node.left, False, True) + dfs(node.right, True, outside)
                )
            else:
                return dfs(node.left, True, True) + dfs(node.right, True, True)

        return dfs(root, True, False)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(root=TreeNode(1,
                        left=TreeNode(2,
                                      TreeNode(3), TreeNode(4))))
        , 2],

    pytest.param(dict(root=TreeNode(1,
                                    left=TreeNode(2, TreeNode(4)),
                                    right=TreeNode(3))), 1)
])
@pytest.mark.parametrize("SolutionCLS", [
    Solution,
])
def test_solutions(kwargs, expected, SolutionCLS):
    assert SolutionCLS().navigation(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
