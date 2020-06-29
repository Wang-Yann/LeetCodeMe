#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数 A 和 B，返回任意字符串 S，要求满足： 
# 
#  
#  S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母； 
#  子串 'aaa' 没有出现在 S 中； 
#  子串 'bbb' 没有出现在 S 中。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：A = 1, B = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
#  
# 
#  示例 2： 
# 
#  输入：A = 4, B = 1
# 输出："aabaa" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A <= 100 
#  0 <= B <= 100 
#  对于给定的 A 和 B，保证存在满足要求的 S。 
#  
#  Related Topics 贪心算法

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        max_val, min_val = max(A, B), min(A, B)
        if max_val > min_val * 2 + 2:
            return ""
        ans = []
        # writeA=False
        while A or B:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                writeA = ans[-1] == "b"
            else:
                writeA = A >= B
            if writeA:
                A -= 1
                ans.append("a")
            else:
                B -= 1
                ans.append("b")
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=1, B=2), ["abb", "bab", "bba"]],
    [dict(A=4, B=1), ["aabaa"]],
    # 无解
    [dict(A=4, B=11), [""]],
])
def test_solutions(kw, expected):
    assert Solution().strWithout3a3b(**kw) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
