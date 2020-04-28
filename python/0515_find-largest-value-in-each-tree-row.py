#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 21:57:24
# @Last Modified : 2020-04-22 21:57:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
from typing import List

from common_utils import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:return []
        result = []
        level =0
        queue = [root]
        while queue:
            length = len(queue)
            result.append(float("-inf"))
            for i in range(length):
                cur = queue.pop(0)
                result[level]=max(result[level],cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level+=1
        return result

if __name__ == '__main__':
    sol = Solution()
    samples=[
        TreeNode(1, left=TreeNode(2, right=TreeNode(4)),
                 right=TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(6))))
    ]
    res = [ sol.largestValues(x) for x in samples]
    print(res)



