#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。 
# 
#  我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。 
# 
#  所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。 
# 
#  请你返回「表现良好时间段」的最大长度。 
# 
#  
# 
#  示例 1： 
# 
#  输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hours.length <= 10000 
#  0 <= hours[i] <= 16 
#  
#  Related Topics 栈

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        N = len(hours)
        arr = [1 if v > 8 else -1 for v in hours]
        prefix = [0]
        for v in arr:
            prefix.append(prefix[-1] + v)
        stack = []
        # 顺序生成单调栈，栈中元素从第一个元素开始严格单调递减，最后一个元素肯定是数组中的最小元素所在位置
        for i in range(N):
            if not stack or prefix[stack[-1]] > prefix[i]:
                stack.append(i)

        i = N
        ans = 0
        # 倒序扫描数组，求最大长度坡
        while i > ans:
            while stack and prefix[stack[-1]] < prefix[i]:
                ans = max(ans, i - stack.pop())
            i -= 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def longestWPI(self, hours: List[int]) -> int:
        """
        We starts with a score = 0,
        If the working hour > 8, we plus 1 point.
        Otherwise we minus 1 point.
        We want find the maximum interval that have strict positive score.

        After one day of work, if we find the total score > 0,
        the whole interval has positive score,
        so we set res = i + 1.

        If the score is a new lowest score, we record the day by seen[cur] = i.
        seen[score] means the first time we see the score is seen[score]th day.

        We want a positive score, so we want to know the first occurrence of score - 1.
        score - x also works, but it comes later than score - 1.
        So the maximum interval is i - seen[score - 1]
        """
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            # print(seen,score)Good 好想法  大1 就代表区段和至少1
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res


@pytest.mark.parametrize("args,expected", [
    (
            [9, 9, 6, 0, 6, 6, 9], 3),
])
def test_solutions(args, expected):
    assert Solution().longestWPI(args) == expected
    assert Solution1().longestWPI(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
