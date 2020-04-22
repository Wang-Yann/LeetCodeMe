#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 21:25:05
# @Last Modified : 2020-04-22 21:25:05
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

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


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(2, left=TreeNode(2)))
    ]
    res = [sol.findMode(x) for x in samples]
    print(res)
