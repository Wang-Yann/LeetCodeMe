#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 22:23:53
# @Last Modified : 2020-04-23 22:23:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。
#
#  添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。
#
#  将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。
#
#  如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。
#
#  示例 1:
#
#
# 输入:
# 二叉树如下所示:
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
# v = 1
#
# d = 2
#
# 输出:
#        4
#       / \
#      1   1
#     /     \
#    2       6
#   / \     /
#  3   1   5
#
#
#
#  示例 2:
#
#
# 输入:
# 二叉树如下所示:
#       4
#      /
#     2
#    / \
#   3   1
#
# v = 1
#
# d = 3
#
# 输出:
#       4
#      /
#     2
#    / \
#   1   1
#  /     \
# 3       1
#
#
#  注意:
#
#
#  输入的深度值 d 的范围是：[1，二叉树最大深度 + 1]。
#  输入的二叉树至少有一个节点。
#
#  Related Topics 树
#  👍 60 👎 0

from common_utils import TreeNode


class Solution:

    def addOneRowMe(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root or not d:
            return root
        level = 1
        if d > 1:
            level_nodes = []
            queue = [root]
            while queue:
                length = len(queue)
                if level == d - 1:
                    level_nodes = queue
                    break
                for i in range(length):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level += 1
            for node in level_nodes:
                tmp_left = node.left
                node.left = TreeNode(v)
                node.left.left = tmp_left
                tmp_right = node.right
                node.right = TreeNode(v)
                node.right.right = tmp_right
        else:
            node = TreeNode(v)
            node.left = root
            return node
        # print(level_nodes)
        return root
    def addOneRow(self, root, v, d):
        """
        """
        if d in (0, 1):
            node = TreeNode(v)
            if d == 1:
                node.left = root
            else:
                node.right = root
            return node
        if root and d >= 2:
            root.left = self.addOneRow(root.left,  v, d-1 if d > 2 else 1)
            root.right = self.addOneRow(root.right, v, d-1 if d > 2 else 0)
        return root




if __name__ == '__main__':
    sol = Solution()
    samples = [
        (TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5))),
         1, 2)

    ]
    res = [sol.addOneRow(*args) for args in samples]
    print(res)
