#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val \
               and self.isSameTree(p.left, q.left) \
               and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, None, 2, 3], [(2, 3)], [(0, 2)]),
        ([1, None, 2, 4], [(2, 3)], [(0, 2)]),
    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    res = [sol.isSameTree(lists[0], lists[1]), sol.isSameTree(lists[0], lists[0])]
    print(res)
