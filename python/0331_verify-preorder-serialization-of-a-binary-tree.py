#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 09:58:52
# @Last Modified : 2020-04-26 09:58:52
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        Good  官方
        想不到
        我们可以定义一个概念，叫做槽位，二叉树中任意一个节点或者空孩子节点都要占据一个槽位。二叉树的建立也伴随着槽位数量的变化。开始时只有一个槽位，如果根节点是空节点，就只消耗掉一个槽位，如果根节点不是空节点，除了消耗一个槽位，还要为孩子节点增加两个新的槽位。之后的节点也是同理
          初始化可用槽位：slots = 1
        """
        data_list = preorder.split(",")
        slots = 1
        for char in data_list:
            slots -= 1
            if slots < 0:
                return False
            if char != "#":
                slots += 2

        return slots == 0


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "9,3,4,#,#,1,#,#,2,#,6,#,#",
        "1,#",
        "9,#,#,1"

    ]
    lists = [x for x in samples]
    res = [sol.isValidSerialization(x) for x in lists]
    print(res)
