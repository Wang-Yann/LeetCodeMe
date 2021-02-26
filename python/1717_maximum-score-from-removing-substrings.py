#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 21:22:30
# @Last Modified : 2021-02-26 21:22:30
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s 和两个整数 x 和 y 。你可以执行下面两种操作任意次。 
# 
#  
#  删除子字符串 "ab" 并得到 x 分。
# 
#  
#  比方说，从 "cabxbae" 删除 ab ，得到 "cxbae" 。 
#  
#  
#  删除子字符串"ba" 并得到 y 分。
#  
#  比方说，从 "cabxbae" 删除 ba ，得到 "cabxe" 。 
#  
#  
#  
# 
#  请返回对 s 字符串执行上面操作若干次能得到的最大得分。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "cdbcbbaaabab", x = 4, y = 5
# 输出：19
# 解释：
# - 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
# - 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
# - 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
# - 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
# 总得分为 5 + 4 + 5 + 5 = 19 。 
# 
#  示例 2： 
# 
#  输入：s = "aabbaaxybbaabb", x = 5, y = 4
# 输出：20
#  
# 
#  
# 
#  提示： 
# 
#  TODO 又吃亏了 显示不准确 10××5
#  1 <= s.length <= 105 
#  1 <= x, y <= 104 
#  s 只包含小写英文字母。 
#  
#  Related Topics 贪心算法 
#  👍 6 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        """
        self.ans = 0
        sub_x, sub_y = "ab", "ba",
        if x < y:
            x, y = y, x
            sub_x, sub_y = sub_y, sub_x

        def helper(cur_s, x, target):
            i = 0
            while i < len(cur_s):
                while cur_s[i:i + 2] == target:
                    self.ans += x
                    cur_s = cur_s[:i] + cur_s[i + 2:]
                    i = max(0, i - 1)
                i += 1
            return cur_s

        s1 = helper(s, x, sub_x)
        helper(s1, y, sub_y)

        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="cdbcbbaaabab", x=4, y=5), 19],
    [dict(s="aabbaaxybbaabb", x=5, y=4), 20],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().maximumGain(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
