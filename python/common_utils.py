#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:52:45
# @Last Modified : 2020-04-07 14:52:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

import os
import sys
import traceback


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def init_list_from_str(cls, s):
        """1->2->3->4->5 """
        if not s:
            return None
        node_list = [cls(int(x.strip())) for x in s.split("->")]
        for i in range(0, len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]

    def __str__(self):
        return "Node[{}]-{}".format(self.val, self.next)
