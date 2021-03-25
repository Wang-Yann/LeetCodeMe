#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 20:55:57
# @Last Modified : 2020-05-02 20:55:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
#
#  若可行，输出任意可行的结果。若不可行，返回空字符串。
#
#  示例 1:
#
#
# 输入: S = "aab"
# 输出: "aba"
#
#
#  示例 2:
#
#
# 输入: S = "aaab"
# 输出: ""
#
#
#  注意:
#
#
#  S 只包含小写字母并且长度在[1, 500]区间内。
#
#  Related Topics 堆 贪心算法 排序 字符串
#  👍 101 👎 0

"""

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


