#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 08:29:03
# @Last Modified : 2021-02-25 08:29:03
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个字符串 s ，它仅包含字符 'a' 和 'b' 。 
# 
#  你可以删除 s 中任意数目的字符，使得 s 平衡 。我们称 s 平衡的 当不存在下标对 (i,j) 满足 i < j 且 s[i] = 'b' 同时 s[
# j]= 'a' 。 
# 
#  请你返回使 s 平衡 的 最少 删除次数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aababbab"
# 输出：2
# 解释：你可以选择以下任意一种方案：
# 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
# 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "bbaaaaabb"
# 输出：2
# 解释：唯一的最优解是删除最前面两个字符。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 105 
#  s[i] 要么是 'a' 要么是 'b' 。 
#  
#  Related Topics 贪心算法 字符串 
#  👍 12 👎 0


import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        GOOD
        Traversing the string from backwards, if a appears first, it could be a misplaced character,
        but we don't know yet. So we keep a count. If b appears first, and no a has appeared, it is always valid, so we can simply ignore it.
        Now what if a has appeared, and b appears? We need to remove either an a or a b.
        It's kind of like a cancelation with each other. And we can decrement the count, meaning one pair of misplacement is gone.
        So we did a deletion, which is either a or b. We don't care whether the actual deletion is a or b, we only care about the number.
        After traversing the entire string, it's guaranteed that the cancelation (deletion) is minimum.
        """
        N = len(s)
        a = 0
        res = 0
        for i in range(N - 1, -1, -1):
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                if a > 0:
                    a -= 1
                    res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="bbaaaaabb"), 2],
    [dict(s="aababbab"), 2],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minimumDeletions(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
