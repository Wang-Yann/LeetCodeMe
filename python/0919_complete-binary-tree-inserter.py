#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:54:46
# @Last Modified : 2020-04-24 22:54:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。
#
#  设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：
#
#
#  CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
#  CBTInserter.insert(int v) 向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的
# 新节点的父节点的值；
#  CBTInserter.get_root() 将返回树的头节点。
#
#
#
#
#
#
#
#  示例 1：
#
#  输入：inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# 输出：[null,1,[1,2]]
#
#
#  示例 2：
#
#  输入：inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4
# ,5,6]],[7],[8],[]]
# 输出：[null,3,4,[1,2,3,4,5,6,7,8]]
#
#
#
#
#  提示：
#
#
#  最初给定的树是完全二叉树，且包含 1 到 1000 个节点。
#  每个测试用例最多调用 CBTInserter.insert 操作 10000 次。
#  给定节点或插入节点的每个值都在 0 到 5000 之间。
#
#  Related Topics 树
#  👍 22 👎 0

"""
from common_utils import TreeNode


class CBTInserter:

    def __init__(self, root: TreeNode):
        self._tree = [root]
        for node in self._tree:
            if node.left:
                self._tree.append(node.left)
            if node.right:
                self._tree.append(node.right)

    def insert(self, v: int) -> int:
        """[1, 2, 3, 4, 5]"""
        n = len(self._tree)
        self._tree.append(TreeNode(v))
        if n % 2:
            self._tree[(n - 1) // 2].left = self._tree[-1]
        else:
            self._tree[(n - 1) // 2].right = self._tree[-1]
        return self._tree[(n - 1) // 2].val

    def get_root(self) -> TreeNode:
        return self._tree[0]


if __name__ == '__main__':
    root = TreeNode(12)
    obj = CBTInserter(root)
    param_1 = obj.insert(3)
    param_3 = obj.insert(4)
    param_2 = obj.get_root()

    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    ob1 = CBTInserter(root1)
    ob1.insert(7)
    ob1.insert(8)
    print(ob1.get_root())
