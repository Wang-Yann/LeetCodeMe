#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 16:05:59
# @Last Modified : 2020-04-20 16:05:59
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:
    """1.递归"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def inorderTraversalRecursive(node, result):
            if node is None:
                return
            inorderTraversalRecursive(node.left, result)
            result.append(node.val)
            inorderTraversalRecursive(node.right, result)

        inorderTraversalRecursive(root, ans)
        return ans


class Solution1:
    """迭代　基于栈"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right

        return ans


class Solution2:
    """
    莫里斯遍历   (可以只需要O(1)空间)
    本方法中，我们使用一种新的数据结构：线索二叉树

    Step 1: 将当前节点current初始化为根节点
    Step 2: While current不为空，
        若current没有左子节点
            a. 将current添加到输出
            b. 进入右子树，亦即, current = current.right
        否则
            a. 在current的左子树中，令current成为最右侧节点的右子节点
            b. 进入左子树，亦即，current = current.left
    """

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        cur = root
        while cur :
            if not cur.left:
                res.append(cur.val)
                cur=cur.right  #// move to next right node
            else: #// has a left subtree
                pre=cur.left
                while pre.right: #// find rightmost
                    pre = pre.right
                pre.right = cur    #// put cur after the pre node
                tmp =cur           #// store cur node
                cur=cur.left       #// move cur to the top of the new tree
                tmp.left=None      #// original cur left be null, avoid infinite loops

        return res


if __name__ == '__main__':
    # sol = Solution()
    sol = Solution2()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([3, 9, 20, None, None, 15, 7], [(0, 1), (2, 5)], [(0, 2), (2, 6)])

    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.inorderTraversal(x) for x in lists]
    print(res)
