#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 17:49:22
# @Last Modified : 2020-04-24 17:49:22
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
#
#  返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
#
#
#
#
#
#  示例 1：
#
#  输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
#
#
#
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#
#
#
#
#  提示：
#
#
#  给定的树是非空的。
#  树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
#  目标结点 target 是树上的结点。
#  0 <= K <= 1000.
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 135 👎 0

import collections
from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        BFS
        不过更改了数据结构,加了父指针
        """
        parent_map = {}

        def dfs(cur, parent):
            if cur:
                parent_map[cur] = parent
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


def test_solutions():
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    K = 2
    res = Solution().distanceK(root, target, K)
    assert res == [7, 4, 1]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
