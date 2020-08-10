#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 21:25:05
# @Last Modified : 2020-04-22 21:25:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#
#  假定 BST 有如下定义：
#
#
#  结点左子树中所含结点的值小于等于当前结点的值
#  结点右子树中所含结点的值大于等于当前结点的值
#  左子树和右子树都是二叉搜索树
#
#
#  例如：
# 给定 BST [1,null,2,2],
#
#     1
#     \
#      2
#     /
#    2
#
#
#  返回[2].
#
#  提示：如果众数超过1个，不需考虑输出顺序
#
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
#  Related Topics 树
#  👍 124 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def findMode(self, root: TreeNode) -> List[int]:
        """ 使用中序遍历解题"""
        if not root:
            return []

        def inorder_traversal(cur, prev, cnt, max_cnt):
            if not cur:
                return prev, cnt, max_cnt
            prev, cnt, max_cnt = inorder_traversal(cur.left, prev, cnt, max_cnt)
            if prev:
                if cur.val == prev.val:
                    cnt += 1
                else:
                    cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
                results.clear()
                results.append(cur.val)
            elif cnt == max_cnt:
                results.append(cur.val)
            return inorder_traversal(cur.right, cur, cnt, max_cnt)

        results = []
        inorder_traversal(root, None, 1, 0)
        return results


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, right=TreeNode(2, left=TreeNode(2))), [2])
])
def test_solutions(args, expected):
    assert Solution().findMode(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
