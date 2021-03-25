#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 特殊的二进制序列是具有以下两个性质的二进制序列： 
# 
#  
#  0 的数量与 1 的数量相等。 
#  二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。 
#  
# 
#  给定一个特殊的二进制序列 S，以字符串形式表示。定义一个操作 为首先选择 S 的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一
# 个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。) 
# 
#  在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？ 
# 
#  示例 1: 
# 
#  
# 输入: S = "11011000"
# 输出: "11100100"
# 解释:
# 将子串 "10" （在S[1]出现） 和 "1100" （在S[3]出现）进行交换。
# 这是在进行若干次操作后按字典序排列最大的结果。
#  
# 
#  说明: 
# 
#  
#  S 的长度不超过 50。 
#  S 保证为一个满足上述定义的特殊 的二进制序列。 
#  
#  Related Topics 递归 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        """
        GOOD
        题中1表示左括号，0表示右括号，即11011000 -> (()(())) 题目条件限定了括号字符串合法，即要合法的括号串并且要字典序最大，
        根据ASCII码左括号应该尽可能多的放在前面。 由于题目给出的已经是有序字符串，所以先递归到最里层，然后一层一层向外扩展，直至完成所有的排序即可
        """
        # print("Call:", S)
        res = []
        anchor, count = 0, 0
        for i, v in enumerate(S):
            count += 1 if v == "1" else -1
            if count == 0:
                res.append("1{}0".format(self.makeLargestSpecial(S[anchor + 1:i])))
                anchor = i + 1
        res.sort(reverse=True)
        # print("S,res:", S, res)
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("11011000", "11100100")
])
def test_solutions(args, expected):
    assert Solution().makeLargestSpecial(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
