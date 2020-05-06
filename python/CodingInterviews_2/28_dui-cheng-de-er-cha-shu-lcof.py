#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 22:57:00
# @Last Modified : 2020-05-06 22:57:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if left and right:
                return left.val == right.val and helper(left.left, right.right) \
                       and helper(right.left, left.right)
            return False

        if not root:
            return True
        return helper(root.left, root.right)
