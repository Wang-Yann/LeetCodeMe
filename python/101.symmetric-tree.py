#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:

        def isSymmetricRecursive(left, right) -> bool:
            if not left and not right:
                return True
            if left and right:
                return left.val == right.val \
                       and isSymmetricRecursive(left.left, right.right) \
                       and isSymmetricRecursive(left.right, right.left)
            return False

        if not root:
            return True
        return isSymmetricRecursive(root.left, root.right)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, 2, 2], [(0, 1)], [(0, 2)]),
        ([1, None, 2, 4], [(2, 3)], [(0, 2)]),
    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.isSymmetric(lists[0]), sol.isSymmetric(lists[1])]
    print(res)
