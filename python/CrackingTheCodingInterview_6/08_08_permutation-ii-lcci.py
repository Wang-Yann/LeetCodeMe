#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:28:01
# @Last Modified : 2020-07-13 11:28:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。 
# 
#  示例1: 
# 
#   输入：S = "qqe"
#  输出：["eqq","qeq","qqe"]
#  
# 
#  示例2: 
# 
#   输入：S = "ab"
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
#  👍 19 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permutation(self, S: str) -> List[str]:
        def dfs(begin):
            if begin == N:
                res.append("".join(chars))
            lookup = set()
            for i in range(begin, N):
                # print(begin,lookup,chars_list)
                if chars[i] in lookup:
                    continue
                lookup.add(chars[i])
                chars[begin], chars[i] = chars[i], chars[begin]
                dfs(begin + 1)
                chars[begin], chars[i] = chars[i], chars[begin]

        res = []
        N = len(S)
        chars = list(S)
        dfs(0)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(S="qqe"), ["eqq", "qeq", "qqe"]],
    # [dict(S="ab"), ["ab", "ba"]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().permutation(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
