#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import pytest

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


class Solution1:

    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            stack.append((p.left, q.right))
            stack.append((p.right, q.left))
        return True


@pytest.mark.parametrize("args,expected", [
    (TreeNode.initTreeSimple([1, 2, 2], [(0, 1)], [(0, 2)]), True),
    (TreeNode.initTreeSimple([1, None, 2, 4], [(2, 3)], [(0, 2)]), False),
])
def test_solutions(args, expected):
    assert Solution().isSymmetric(args) == expected
    assert Solution1().isSymmetric(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
