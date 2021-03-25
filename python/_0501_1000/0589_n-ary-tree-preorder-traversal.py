#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 17:08:00
# @Last Modified : 2020-04-22 17:08:00
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个 N 叉树，返回其节点值的前序遍历。
#
#  例如，给定一个 3叉树 :
#
#
#
#
#
#
#
#  返回其前序遍历: [1,3,5,6,2,4]。
#
#
#
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树
#  👍 89 👎 0

from typing import List

import pytest

from common_utils import TreeNodeWithChildren as Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        results = []
        stack = [root]
        while stack:
            cur = stack.pop()
            results.append(cur.val)
            children = cur.children
            if children:
                for child in children[::-1]:
                    stack.append(child)

        return results


@pytest.mark.parametrize("kw,expected", [
    [dict(root=Node(1, [Node(3, [Node(5), Node(6)]),
                        Node(2),
                        Node(4)
                        ]
                    )), [1, 3, 5, 6, 2, 4]],
])
def test_solutions(kw, expected):
    assert Solution().preorder(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
