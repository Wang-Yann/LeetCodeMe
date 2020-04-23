#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 22:48:32
# @Last Modified : 2020-04-23 22:48:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            length = len(queue)
            sum = 0
            for i in range(length):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum / length)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    ]
    res = [sol.averageOfLevels(args) for args in samples]
    print(res)
