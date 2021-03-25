#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 17:29:49
# @Last Modified : 2020-07-31 17:29:49
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的子序列。 
# 
#  给定源字符串 source 和目标字符串 target，找出源字符串中能通过串联形成目标字符串的子序列的最小数量。如果无法通过串联源字符串中的子序列来构造
# 目标字符串，则返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：source = "abc", target = "abcbc"
# 输出：2
# 解释：目标字符串 "abcbc" 可以由 "abc" 和 "bc" 形成，它们都是源字符串 "abc" 的子序列。
#  
# 
#  示例 2： 
# 
#  输入：source = "abc", target = "acdbc"
# 输出：-1
# 解释：由于目标字符串中包含字符 "d"，所以无法由源字符串的子序列构建目标字符串。
#  
# 
#  示例 3： 
# 
#  输入：source = "xyz", target = "xzyxz"
# 输出：3
# 解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。
#  
# 
#  
# 
#  提示： 
# 
#  
#  source 和 target 两个字符串都只包含 "a"-"z" 的英文小写字母。 
#  source 和 target 两个字符串的长度介于 1 和 1000 之间。 
#  
#  Related Topics 贪心算法 动态规划 
#  👍 23 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """代码清晰"""
        count = 0
        s = 0
        t = 0
        while t < len(target):
            if target[t] not in source:
                return -1
            if source[s] == target[t]:
                s += 1
                t += 1
            else:
                s += 1
            if s >= len(source):
                count += 1
                s = 0
        if t >= len(target) and s != 0:
            count += 1
        return count


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def shortestWay(self, source: str, target: str) -> int:
        """GOOD"""
        N = len(target)
        s = source * N
        r, cur = len(s) - 1, N - 1
        while cur >= 0 and r >= 0:
            if s[r] == target[cur]:
                cur -= 1
            r -= 1
        # print("cur,r",cur,r)
        if cur >= 0:
            return -1
        return N - (r + 1) // len(source)


@pytest.mark.parametrize("kw,expected", [
    [dict(source="abc", target="abcbc"), 2],
    [dict(source="abc", target="acdbc"), -1],
    [dict(source="xyz", target="xzyxz"), 3],
])
def test_solutions(kw, expected):
    assert Solution().shortestWay(**kw) == expected
    assert Solution1().shortestWay(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
