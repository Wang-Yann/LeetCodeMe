#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 17:49:22
# @Last Modified : 2020-04-24 17:49:22
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
from typing import List

from common_utils import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        BFS
        不过更改了数据结构,加了父指针
        """
        parent_map={}
        def dfs(cur, parent):
            if cur:
                parent_map[cur]=parent
                # cur.parent = parent
                dfs(cur.left, cur)
                dfs(cur.right, cur)

        dfs(root, None)
        dq = collections.deque([(target, 0)])
        is_visited = {target}
        while dq:
            if dq[0][1] == K:
                return [node.val for node, level in dq]
            cur, level = dq.popleft()
            for nd in (cur.left, cur.right, parent_map[cur]):
                if nd and nd not in is_visited:
                    is_visited.add(nd)
                    dq.append((nd, level + 1))
        return []


if __name__ == '__main__':
    sol = Solution()

    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    K = 2
    res = sol.distanceK(root, target, K)
    print(res)
