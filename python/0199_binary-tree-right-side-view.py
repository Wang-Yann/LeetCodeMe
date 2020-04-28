#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:12:31
# @Last Modified : 2020-04-22 10:12:31
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
from collections import deque
from typing import List

from common_utils import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:return ans
        queue = deque([root])
        while queue:
            level_length = len(queue)
            ans.append(queue[level_length-1].val)
            for i in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
    TreeNode(1,
        left=TreeNode(2, right=TreeNode(5)),
        right=TreeNode(3, right=TreeNode(4))
    )]
    lists = [x for x in samples]
    res = [sol.rightSideView(x) for x in lists]
    print(res)
