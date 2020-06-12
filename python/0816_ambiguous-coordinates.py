#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表
# 中。 
# 
#  原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数
# 来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。 
# 
#  最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。 
# 
#  
# 
#  
# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
#  
# 
#  
# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释: 
# 0.0, 00, 0001 或 00.01 是不被允许的。
#  
# 
#  
# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 
# 3)"]
#  
# 
#  
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释: 
# 1.0 是不被允许的。
#  
# 
#  
# 
#  提示: 
# 
#  
#  4 <= S.length <= 12. 
#  S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。 
#  
# 
#  
#  Related Topics 字符串

"""
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        length = len(S)

        def make(i, n):
            for d in range(1, n + 1):
                left = S[i:i + d]
                right = S[i + d:i + n]
                if ((not left.startswith("0") or left == "0")
                        and (not right.endswith("0"))
                ):
                    yield "".join([left, "." if right else "", right])

        ans = []
        for i in range(1, length - 2):
            for cand in itertools.product(make(1, i), make(i + 1, length - 2 - i)):
                # print(cand)
                ans.append("({}, {})".format(*cand))
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("(123)", ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]),
    ("(00011)", ["(0.001, 1)", "(0, 0.011)"]),
    ("(0123)", ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]),
    ("(100)", ["(10, 0)"]),
])
def test_solutions(args, expected):
    assert sorted(Solution().ambiguousCoordinates(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
