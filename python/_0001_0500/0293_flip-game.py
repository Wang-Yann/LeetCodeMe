#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 14:05:04
# @Last Modified : 2020-07-27 14:05:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你和朋友玩一个叫做「翻转游戏」的游戏，游戏规则：给定一个只有 + 和 - 的字符串。你和朋友轮流将 连续 的两个 "++" 反转成 "--"。 当一方无法进
# 行有效的翻转时便意味着游戏结束，则另一方获胜。 
# 
#  请你写出一个函数，来计算出第一次翻转后，字符串所有的可能状态。 
# 
#  
# 
#  示例： 
# 
#  输入: s = "++++"
# 输出: 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
#  
# 
#  注意：如果不存在可能的有效操作，请返回一个空列表 []。 
#  Related Topics 字符串 
#  👍 15 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                ans.append(s[:i] + "--" + s[i + 2:])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="++++"), [
        "--++",
        "+--+",
        "++--"
    ]
     ],
])
def test_solutions(kw, expected):
    assert sorted(Solution().generatePossibleNextMoves(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
