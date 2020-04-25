#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:35:15
# @Last Modified : 2020-04-24 22:35:15
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        cur = root
        stack = []
        res = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        new_root = TreeNode(res[0])
        cur = new_root
        for i in range(1, len(res) ):
            cur.right = TreeNode(res[i])
            cur = cur.right
        return new_root


class Solution1:
    """具体地，当我们遍历到一个节点时，把它的左孩子设为空，并将其本身作为上一个遍历到的节点的右孩子。"""

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(cur, pre):
            if not cur:
                return pre
            result = helper(cur.left, cur)
            cur.left = None
            cur.right = helper(cur.right, pre)
            return result

        return helper(root, None)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)))
    ]
    res = [sol.increasingBST(args) for args in samples]
    print(res)
