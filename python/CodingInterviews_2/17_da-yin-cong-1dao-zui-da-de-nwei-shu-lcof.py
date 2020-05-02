#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 22:01:25
# @Last Modified : 2020-05-02 22:01:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1,10**n))

@pytest.mark.parametrize("args,expected", [
    (1, [1,2,3,4,5,6,7,8,9]),
])
def test_solutions(args, expected):
    assert Solution().printNumbers(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


