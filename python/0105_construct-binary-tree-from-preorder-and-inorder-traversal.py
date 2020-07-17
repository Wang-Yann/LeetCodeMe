#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 10:52:40
# @Last Modified : 2020-04-21 10:52:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics 树 深度优先搜索 数组
#  👍 573 👎 0

import copy
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        """
        因为前序遍历为根左右。 中序遍历为左根右。
        所以前序遍历的第一个元素为重建的二叉树的根节点的值。
        遍历中序遍历，直到找到和根节点值相同的位置。
        则此元素左边的都是根节点的左子树的元素，右边的都是根节点右子树的元素。

        """
        if not preorder and inorder: return None
        inorder_lookup = {v: idx for idx, v in enumerate(inorder)}

        def buildTreeRecursive(pre_start, in_start, in_end):
            if in_start == in_end:
                return None
            node_val = preorder[pre_start]
            node = TreeNode(node_val)
            idx = inorder_lookup[node_val]
            # print("pre_start,idx,in_start", pre_start,idx ,in_start)
            node.left = buildTreeRecursive(pre_start + 1, in_start, idx)
            # 得到左子树中的节点数目 idx - in_start
            node.right = buildTreeRecursive(pre_start + 1 + idx - in_start, idx + 1, in_end)
            return node

        return buildTreeRecursive(0, 0, len(inorder))

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and inorder: return None
        inorder_lookup = {v: idx for idx, v in enumerate(inorder)}
        pre_idx = 0

        def helper(in_start, in_end):
            nonlocal pre_idx
            if in_start == in_end:
                return None
            node_val = preorder[pre_idx]
            node = TreeNode(node_val)
            index = inorder_lookup[node_val]
            pre_idx += 1
            node.left = helper(in_start, index)
            node.right = helper(index + 1, in_end)
            return node

        return helper(0, len(inorder))

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and inorder: return None
        inorder_lookup = {v: idx for idx, v in enumerate(inorder)}

        # pre_idx = 0

        def helper(in_start, in_end):
            # nonlocal pre_idx
            if in_start == in_end:
                return None
            node_val = preorder.pop(0)
            node = TreeNode(node_val)
            index = inorder_lookup[node_val]
            # pre_idx += 1
            node.left = helper(in_start, index)
            node.right = helper(index + 1, in_end)
            return node

        return helper(0, len(inorder))


class Solution9:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not inorder: return None # inorder is empty
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
        return root

@pytest.mark.parametrize("args,expected",[
   [([3, 9, 20, 15, 7],[9, 3, 15, 20, 7]),
    TreeNode.initPreOrder([3, 9,None,None, 20,15,None,None, 7,None,None  ]) ]
])
def test_solutions(args,expected):
    assert repr(Solution().buildTree(*copy.deepcopy(args)))==repr(expected)
    assert repr(Solution().buildTree1(*copy.deepcopy(args)))==repr(expected)
    assert repr(Solution().buildTree2(*copy.deepcopy(args)))==repr(expected)
    assert repr(Solution9().buildTree(*copy.deepcopy(args)))==repr(expected)

if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])
