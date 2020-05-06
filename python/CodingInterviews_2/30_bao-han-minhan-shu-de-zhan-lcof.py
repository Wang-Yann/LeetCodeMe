#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 23:17:56
# @Last Modified : 2020-05-06 23:17:56
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]


    def push(self, x: int) -> None:
        if self.stack:
            current_min=min(x,self.stack[-1][0])
            self.stack.append((current_min,x))
        else:
            self.stack.append((x,x))




    def pop(self) -> None:
        return self.stack.pop()[1]


    def top(self) -> int:
        return self.stack[-1][1]


    def min(self) -> int:
        return self.stack[-1][0]




