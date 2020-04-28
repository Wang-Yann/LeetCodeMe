#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 14:30:39
# @Last Modified : 2020-04-22 14:30:39
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List

from common_utils import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        results= []
        def dfs(path,node):
            if not node:
                return
            if not node.left and not node.right:
                results.append(path+[node.val])
            dfs(path+[node.val],node.left)
            dfs(path+[node.val],node.right)
        dfs([],root)
        return ["->".join(map(str,x)) for x in results]



if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(5,
                 left=TreeNode(6),
                 right=TreeNode(2, TreeNode(7), TreeNode(4))
                 ) ,
        TreeNode(12),
        None

    ]
    lists = [ x for x in samples  ]
    res = [sol.binaryTreePaths(x) for x in lists]
    print(res)


