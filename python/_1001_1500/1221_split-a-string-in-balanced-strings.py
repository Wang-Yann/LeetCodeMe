#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。 
# 
#  给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。 
# 
#  返回可以通过分割得到的平衡字符串的最大数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "RLRRLLRLRL"
# 输出：4
# 解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。
#  
# 
#  示例 2： 
# 
#  输入：s = "RLLLLRRRLR"
# 输出：3
# 解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。
#  
# 
#  示例 3： 
# 
#  输入：s = "LLLLRRRR"
# 输出：1
# 解释：s 只能保持原样 "LLLLRRRR".
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s[i] = 'L' 或 'R' 
#  分割得到的每个字符串都必须是平衡字符串。 
#  
#  Related Topics 贪心算法 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """AC Good 30s解决
        恢复信心
        """
        level = 0
        ans = 0
        for char in s:
            if char == "L":
                level += 1
            else:
                level -= 1
            if level == 0:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kw,expected", [
    [dict(s="RLRRLLRLRL"), 4],
    [dict(s="RLLLLRRRLR"), 3],
    [dict(s="LLLLRRRR"), 1],
])
def test_solutions(kw, expected):
    assert Solution().balancedStringSplit(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
