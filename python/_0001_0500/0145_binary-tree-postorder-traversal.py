#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-20 15:52:08
# @Last Modified : 2020-04-20 15:52:08
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，返回它的 后序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 345 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution1:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(node, result):
            if node is None:
                return
            helper(node.left, result)
            helper(node.right, result)
            result.append(node.val)

        helper(root, res)
        return res


class Solution0:
    """迭代　稍复杂"""

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
       TODO
       在做迭代前序遍历和中序遍历的时候，发现root经过的路径都是左根右，对于前序和中序来说，访问路径基本上跟经过路径是一致的。
       但是在后序遍历中，我们先经过根节点，但是我们不会去访问它，
       而是会选择先访问它的右子节点。所以在这种情况下，我们会将根节点留在栈中不弹出，等到需要访问它的时候再出。

        那我们什么情况下才能访问根节点？是从右节点回溯到根节点，而不是从左节点回溯到根节点，所以我们需要记录之前结点和当前节点的关系，
        来确定是否访问当前节点。总结起来，我们什么时候才能访问节点。有如下两种情况：

        当前经过节点是叶子节点。
        当前经过节点的右子节点是上一次访问的节点。
        若不满足上述情况，说明是从左孩子回溯到根节点，需要先访问根节点的右孩子，root = root.right
        """
        if not root:
            return []
        res = []  ## //用于存放访问顺序
        stack = []  ## //存放结点，用于回溯
        pre, cur = None, root  ## //记录之前访问过的结点
        while cur or stack:  ## //迭代访问二叉树
            while cur:  ## //使root指向当前子二叉树的最左结点
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if cur.right is None or cur.right == pre:  ## //当前结点为叶子结点 或者 当前结点的右孩子是上个访问结点
                pre = cur  ## //更新上一次访问的结点
                res.append(stack.pop().val)  ## //出栈，表示访问了当前结点
                cur = None  ## //让root到下一次循环再更新，避免发生空栈错误
            else:
                cur = cur.right  ## //访问当前结点的右孩子

        return res


class Solution:
    """
    迭代　标记法
    TODO
    """

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], [(root, False)]
        while stack:
            node, is_visited = stack.pop()
            if node is None:
                continue
            if is_visited:
                result.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, right=TreeNode(2, left=TreeNode(3)))), [3, 2, 1]],
])
def test_solutions(kw, expected):
    assert Solution().postorderTraversal(**kw) == expected
    assert Solution0().postorderTraversal(**kw) == expected
    assert Solution1().postorderTraversal(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
