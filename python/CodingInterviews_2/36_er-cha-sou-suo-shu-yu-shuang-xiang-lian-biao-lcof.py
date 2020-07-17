#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-09 22:47:36
# @Last Modified : 2020-05-09 22:47:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest

from common_utils import TreeNode as Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
        solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
        画图
        """
        self.pre = None
        self.head = None

        def dfs(cur):
            if not cur:
                return None
            dfs(cur.left)
            if self.pre:
                # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:
                # 记录头节点
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
