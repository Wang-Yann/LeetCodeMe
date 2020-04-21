#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 10:52:40
# @Last Modified : 2020-04-21 10:52:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

    ]
    lists = [x for x in samples]
    res = [sol.buildTree(*x) for x in lists]
    print(res)
