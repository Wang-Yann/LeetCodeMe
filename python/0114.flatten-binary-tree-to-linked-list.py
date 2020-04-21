#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 20:47:39
# @Last Modified : 2020-04-21 20:47:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def flattenS(self, root: TreeNode) -> None:
        """
        TODO
        """

        def flattenRec(node, list_head):
            if node:
                list_head = flattenRec(node.right, list_head)
                list_head = flattenRec(node.left, list_head)
                node.right = list_head
                node.left = None
                return node
            else:
                # print(node,list_head)
                return list_head

        flattenRec(root, None)

    def flatten(self, root: TreeNode) -> None:
        """
        特殊的先序遍历，提前将右孩子保存到栈中，我们利用这种遍历方式就可以防止右孩子的丢失了。由于栈是先进后出，所以我们先将右节点入栈
        """
        if not root:
            return
        stack = [root]
        pre = None
        while stack:
            tmp = stack.pop()
            if  pre:
                pre.right = tmp
                pre.left = None
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
            pre = tmp


if __name__ == '__main__':
    sol = Solution()
    samples = [
        # ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)]),
        # ([1], [], [])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.flatten(x) for x in lists]
    print(lists)
