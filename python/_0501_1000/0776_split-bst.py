#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 16:27:47
# @Last Modified : 2020-07-31 16:27:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给你一棵二叉搜索树（BST）、它的根结点 root 以及目标值 V。
# 
#  请将该树按要求拆分为两个子树：其中一个子树结点的值都必须小于等于给定的目标值 V；另一个子树结点的值都必须大于目标值 V；树中并非一定要存在值为 V 的结
# 点。 
# 
#  除此之外，树中大部分结构都需要保留，也就是说原始树中父节点 P 的任意子节点 C，假如拆分后它们仍在同一个子树中，那么结点 P 应仍为 C 的子结点。 
# 
#  你需要返回拆分后两个子树的根结点 TreeNode，顺序随意。 
# 
#  
# 
#  示例： 
# 
#  输入：root = [4,2,6,1,3,5,7], V = 2
# 输出：[[2,1],[4,3,6,null,null,5,7]]
# 解释：
# 注意根结点 output[0] 和 output[1] 都是 TreeNode 对象，不是数组。
# 
# 给定的树 [4,2,6,1,3,5,7] 可化为如下示意图：
# 
#           4
#         /   \
#       2      6
#      / \    / \
#     1   3  5   7
# 
# 输出的示意图如下：
# 
#           4
#         /   \
#       3      6       和    2
#             / \           /
#            5   7         1 
# 
#  
# 
#  提示： 
# 
#  
#  二叉搜索树节点个数不超过 50 
#  二叉搜索树始终是有效的，并且每个节点的值都不相同 
#  
#  Related Topics 树 递归 
#  👍 44 👎 0


from typing import List

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
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        """
        GOOD
        根节点要么在第一棵子树中，要么在第二棵子树中。假设根节点在第一棵子树中，那么这棵树的左子树一定在第一棵子树中，
        右子树中部分节点在第一棵子树，部分在第二棵子树中

        p0,p1为分割树的结果。 p0,p1 在分割之后依然还是二叉搜索树，其中p0 在第一棵子树中，p1 为第二棵子树
        """
        if not root:
            return [None, None]
        elif root.val <= V:
            # p0,p1 对应小于等于V的part,大于的
            p0, p1 = self.splitBST(root.right, V)
            root.right = p0
            return [root, p1]
        else:
            p0, p1 = self.splitBST(root.left, V)
            root.left = p1
            return [p0, root]


# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    p1 = TreeNode(4, left=TreeNode(3), right=TreeNode(6, TreeNode(5), TreeNode(7)))
    p2 = TreeNode(2, left=TreeNode(1))
    root = TreeNode(
        4,
        left=TreeNode(2, TreeNode(1), TreeNode(3)),
        right=TreeNode(6, TreeNode(5), TreeNode(7))
    )
    res = Solution().splitBST(root, 2)
    assert sorted([repr(x) for x in res]) == [repr(p2), repr(p1)]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
