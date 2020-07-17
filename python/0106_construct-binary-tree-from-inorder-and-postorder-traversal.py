#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-21 10:52:40
# @Last Modified : 2020-04-21 10:52:40
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 根据一棵树的中序遍历与后序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  Related Topics 树 深度优先搜索 数组
#  👍 242 👎 0

from typing import List

from common_utils import TreeNode


class Solution:
    def buildTreeS(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        """
        因为前序遍历为根左右。 中序遍历为左根右。
        所以前序遍历的第一个元素为重建的二叉树的根节点的值。
        遍历中序遍历，直到找到和根节点值相同的位置。
        则此元素左边的都是根节点的左子树的元素，右边的都是根节点右子树的元素。

        """
        if not postorder and inorder: return None
        inorder_lookup = {v: idx for idx, v in enumerate(inorder)}

        def buildTreeRecursive(post_end, in_start, in_end):
            if in_start == in_end:
                return None
            node_val = postorder[post_end - 1]
            node = TreeNode(node_val)
            idx = inorder_lookup[node_val]
            print("post_end,idx,in_start", post_end, idx, in_end)
            node.left = buildTreeRecursive(post_end - 1 - (in_end - idx - 1), in_start, idx)
            node.right = buildTreeRecursive(post_end - 1, idx + 1, in_end)
            return node

        return buildTreeRecursive(0, 0, len(inorder))

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_lookup = {v: idx for idx, v in enumerate(inorder)}

        def helper(in_start, in_end):
            if in_start == in_end:
                return None
            node_val = postorder.pop()
            node = TreeNode(node_val)
            index = inorder_lookup[node_val]
            # print("Node", node_val, in_start, in_end)
            node.right = helper(index + 1, in_end)
            node.left = helper(in_start, index)
            return node

        return helper(0, len(inorder) )


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])

    ]
    lists = [x for x in samples]
    res = [sol.buildTree(*x) for x in lists]
    print(res)
