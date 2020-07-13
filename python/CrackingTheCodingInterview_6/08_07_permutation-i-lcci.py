#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:14:57
# @Last Modified : 2020-07-13 11:14:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。 
# 
#  示例1: 
# 
#  
#  输入：S = "qwe"
#  输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
#  
# 
#  示例2: 
# 
#  
#  输入：S = "ab"
#  输出：["ab", "ba"]
#  
# 
#  提示: 
# 
#  
#  字符都是英文字母。 
#  字符串长度在[1, 9]之间。 
#  
#  Related Topics 回溯算法 
#  👍 21 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, S: str) -> List[str]:
        def backtrack(begin):
            if begin == N:
                res.append("".join(chars_list))
            for i in range(begin, N):
                chars_list[begin], chars_list[i] = chars_list[i], chars_list[begin]
                backtrack(begin + 1)
                chars_list[begin], chars_list[i] = chars_list[i], chars_list[begin]

        res = []
        N = len(S)
        chars_list = list(S)
        backtrack(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(S="qwe"), ["qwe", "qew", "wqe", "weq", "ewq", "eqw"]],
    [dict(S="ab"), ["ab", "ba"]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().permutation(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
