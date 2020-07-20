#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 22:52:38
# @Last Modified : 2020-05-06 22:52:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
#  例如输入：
#
#  4
#  / \
#  2 7
#  / \ / \
# 1 3 6 9
# 镜像输出：
#
#  4
#  / \
#  7 2
#  / \ / \
# 9 6 3 1
#
#
#
#  示例 1：
#
#  输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 1000
#
#  注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/
#  Related Topics 树
#  👍 37 👎 0
import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:return None
        root.left = self.mirrorTree(root.right)
        root.right=self.mirrorTree(root.left)
        return root






