#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 21:44:06
# @Last Modified : 2020-04-10 21:44:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback

import pytest


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))




@pytest.mark.parametrize("args,expected", [
    ("the sky is blue", "blue is sky the"),
    ("  hello world!  ", "world! hello"),
    ("a good   example", "example good a"),
])
def test_solutions(args, expected):
    assert Solution().reverseWords(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

























