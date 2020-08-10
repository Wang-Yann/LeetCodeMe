#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 18:23:41
# @Last Modified : 2020-04-24 18:23:41
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定一个根为 root 的二叉树，每个结点的深度是它到根的最短距离。
#
#  如果一个结点在整个树的任意结点之间具有最大的深度，则该结点是最深的。
#
#  一个结点的子树是该结点加上它的所有后代的集合。
#
#  返回能满足“以该结点为根的子树中包含所有最深的结点”这一条件的具有最大深度的结点。
#
#
#
#  示例：
#
#  输入：[3,5,1,6,2,0,8,null,null,7,4]
# 输出：[2,7,4]
# 解释：
#
# 我们返回值为 2 的结点，在图中用黄色标记。
# 在图中用蓝色标记的是树的最深的结点。
# 输入 "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" 是对给定的树的序列化表述。
# 输出 "[2, 7, 4]" 是对根结点的值为 2 的子树的序列化表述。
# 输入和输出都具有 TreeNode 类型。
#
#
#
#
#  提示：
#
#
#  树中结点的数量介于 1 和 500 之间。
#  每个结点的值都是独一无二的。
#
#  Related Topics 树
#  👍 72 👎 0

"""
import collections

import pytest

from common_utils import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return root
        Result = collections.namedtuple("Result", ("node", "depth"))

        def dfs(cur):
            """
            Return node,depth
            题意有含糊
            """
            if not cur:
                return Result(None, 0)
            left_res, right_res = dfs(cur.left), dfs(cur.right)
            if left_res.depth > right_res.depth:
                return Result(left_res.node, left_res.depth + 1)
            elif left_res.depth < right_res.depth:
                return Result(right_res.node, right_res.depth + 1)
            else:
                return Result(cur, left_res.depth + 1)

        result = dfs(root)
        return result.node


def test_solution():
    sol = Solution()
    target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
    root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))
    res = sol.subtreeWithAllDeepest(root)
    assert repr(res) == str(['2', '7', '4'])


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
