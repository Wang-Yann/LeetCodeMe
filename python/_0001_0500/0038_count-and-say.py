#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下： 
# 
#  1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#  
# 
#  1 被读作 "one 1" ("一个一") , 即 11。 
# 11 被读作 "two 1s" ("两个一"）, 即 21。 
# 21 被读作 "one 2", "one 1" （"一个二" , "一个一") , 即 1211。 
# 
#  给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。 
# 
#  注意：整数序列中的每一项将表示为一个字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: "1"
# 解释：这是一个基本样例。 
# 
#  示例 2: 
# 
#  输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 
# "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。 
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countAndSay(self, n: int) -> str:
        def getNext(seq):
            i, next_seq = 0, ""
            while i <= len(seq) - 1:
                cnt = 1
                while i <= len(seq) - 2 and seq[i] == seq[i + 1]:
                    cnt += 1
                    i += 1
                next_seq += str(cnt) + seq[i]
                i += 1
            return next_seq

        seq = "1"
        for i in range(n - 1):
            seq = getNext(seq)
        return seq

    # leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, "1"),
    (4, "1211"),
])
def test_solutions(args, expected):
    assert Solution().countAndSay(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
