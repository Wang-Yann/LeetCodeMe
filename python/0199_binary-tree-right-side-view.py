#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:12:31
# @Last Modified : 2020-04-22 10:12:31
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#  示例:
#
#  输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 277 👎 0

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
