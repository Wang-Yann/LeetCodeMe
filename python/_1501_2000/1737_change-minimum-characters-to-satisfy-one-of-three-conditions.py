#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 12:34:04
# @Last Modified : 2021-02-27 12:34:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你两个字符串 a 和 b ，二者均由小写字母组成。一步操作中，你可以将 a 或 b 中的 任一字符 改变为 任一小写字母 。 
# 
#  操作的最终目标是满足下列三个条件 之一 ： 
# 
#  
#  a 中的 每个字母 在字母表中 严格小于 b 中的 每个字母 。 
#  b 中的 每个字母 在字母表中 严格小于 a 中的 每个字母 。 
#  a 和 b 都 由 同一个 字母组成。 
#  
# 
#  返回达成目标所需的 最少 操作数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = "aba", b = "caa"
# 输出：2
# 解释：满足每个条件的最佳方案分别是：
# 1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
# 2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
# 3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
# 最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。
#  
# 
#  示例 2： 
# 
#  输入：a = "dabadd", b = "cda"
# 输出：3
# 解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= a.length, b.length <= 105 
#  a 和 b 只由小写字母组成 
#  
#  Related Topics 贪心算法 字符串 
#  👍 33 👎 0
  

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minCharacters(self, a: str, b: str) -> int:
        """
        condition 3 with m + n - most_common.

        The we calculate the accumulate prefix sum of count.
        This help finding the number of smaller characters in O(1) time.

        Enumerate the character i a,b,c...x,y,
        To meet condition 1,
        which is a < b,
        we need (m - c1[i]) + c2[i]

        To meet condition 2,
        which is a > b,
        we need n - c2[i] + c1[i]
        """
        m, n = len(a), len(b),
        c1, c2 = collections.Counter(ord(x) - ord("a") for x in a), collections.Counter(ord(x) - ord("a") for x in b),
        res = m + n - max((c1 + c2).values())
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            res = min(res, m - c1[i] + c2[i]) # condition 1
            res = min(res, n - c2[i] + c1[i]) # condition 2
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(a="aba", b="caa"), 2],
    [dict(a="dabadd", b="cda"), 3],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minCharacters(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
