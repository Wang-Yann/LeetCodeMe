#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 21:34:22
# @Last Modified : 2020-04-24 21:34:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

from common_utils import TreeNode


class Solution1:

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        todo
        hard
        """
        if not (pre and post):
            return None
        stack = [TreeNode(pre[0])]
        j = 0
        for i in range(1, len(pre)):
            node = TreeNode(pre[i])
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]


class Solution:

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        """
        官方

        前序遍历为：
        (根结点) (前序遍历左分支) (前序遍历右分支)
        而后序遍历为：

        (后序遍历左分支) (后序遍历右分支) (根结点)
        我们令左分支有 LL 个节点。我们知道左分支的头节点为 pre[1]，但它也出现在左分支的后序表示的最后。所以 pre[1] = post[L-1]（因为结点的值具有唯一性），
        因此 L = post.indexOf(pre[1]) + 1

        """
        if not (pre and post):
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        dict(pre=[1, 2, 4, 5, 3, 6, 7], post=[4, 5, 2, 6, 7, 3, 1]),
        dict(pre=[1], post=[1])
    ]
    res = [sol.constructFromPrePost(**args) for args in samples]
    print(res)
