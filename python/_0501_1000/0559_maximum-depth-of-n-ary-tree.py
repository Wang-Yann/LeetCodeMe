#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 14:56:02
# @Last Modified : 2020-04-23 14:56:02
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个 N 叉树，找到其最大深度。
#
#  最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  我们应返回其最大深度，3。
#
#  说明:
#
#
#  树的深度不会超过 1000。
#  树的节点总不会超过 5000。
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 98 👎 0
import pytest

from common_utils import TreeNodeWithChildren as Node


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max([self.maxDepth(node) for node in root.children]) + 1


@pytest.mark.parametrize("kw,expected", [
    [dict(root=Node(1, [Node(3, [Node(5), Node(6)]),
                        Node(2),
                        Node(4)]
                    )), 3],
])
def test_solutions(kw, expected):
    assert Solution().maxDepth(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
