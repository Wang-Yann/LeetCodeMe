#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 20:55:57
# @Last Modified : 2020-05-02 20:55:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import traceback
import pytest
from typing import List

class Solution:
    def reorganizeString(self, S: str) -> str:
        length = len(S)
        A =[]
        for cnt,x in sorted([(S.count(x),x) for x in set(S)]):
            if cnt>(length+1)//2:return ""
            A.extend(cnt*x)
        ans =[None]*length
        ans[::2],ans[1::2] = A[length//2:],A[:length//2]
        # print(A,ans)
        return "".join(ans)


@pytest.mark.parametrize("args,expected", [
    ("aab", "aba"),
    pytest.param("aaab",""),
])
def test_solutions(args, expected):
    assert Solution().reorganizeString(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


