#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:41:32
# @Last Modified : 2020-04-24 16:41:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """TODO
        注意
        if not root.left and not root.right and root.val == 0:
            return None
        判断放在上面得出不了正确结果,思考下为什么 ：
        需要后序遍历
        """
        if not root:
            return None
        # if not root.left and not root.right and root.val == 0:
        #     return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(0, TreeNode(0), TreeNode(1))),
        TreeNode(0, right=TreeNode(1, TreeNode(0), TreeNode(1))),

    ]
    lists = [x for x in samples]
    res = [sol.pruneTree(x) for x in lists]
    print(res)
