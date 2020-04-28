#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 22:23:53
# @Last Modified : 2020-04-23 22:23:53
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
