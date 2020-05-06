#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 22:52:38
# @Last Modified : 2020-05-06 22:52:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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






