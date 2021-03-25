#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。 
# 
#  示例： 
# 
#  输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC" 
# 
#  说明： 
# 
#  
#  如果 S 中不存这样的子串，则返回空字符串 ""。 
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    滑动窗口
    https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/
    """

    def minWindow(self, s: str, t: str) -> str:
        """Good"""
        if not t or not s:
            return ""
        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        # left and right pointer
        l, r = 0, 0
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                # Move the left pointer ahead, this would help to look for a new window.
                l += 1
            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def minWindow(self, s: str, t: str) -> str:
        score = 0
        wanted = collections.Counter(t)
        start, end = len(s), 3 * len(s)
        d = collections.defaultdict(int)
        deq = collections.deque([])
        for idx, char in enumerate(s):
            if char in wanted:
                deq.append(idx)
                d[char] += 1
                if d[char] <= wanted[char]:
                    score += 1
                while deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
                    d[s[deq.popleft()]] -= 1
                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]
        return s[start:end + 1]


class Solution2:

    def minWindow(self, s: str, t: str) -> str:
        """
        https://leetcode-cn.com/problems/minimum-window-substring/solution/python-jian-ji-hua-dong-chuang-kou-xiang-jie-by-am/
        """
        counter = collections.Counter(t)
        ans = ""
        cnt = 0  # 当前我满足了 t 中的字母的种数
        l = 0
        for r, r_char in enumerate(s):
            if r_char not in counter:
                continue
            counter[r_char] -= 1
            if counter[r_char] == 0:
                cnt += 1
            while s[l] not in counter or counter[s[l]] < 0:  # 看看当前 l 处的字母是否必要，没必要 l 就加以
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1
            if cnt == len(counter):
                if not ans or len(ans) > r - l + 1:
                    ans = s[l: r + 1]
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(s="ADOBECODEBANC", t="ABC"), "BANC"),
])
def test_solutions(kwargs, expected):
    assert Solution().minWindow(**kwargs) == expected
    assert Solution1().minWindow(**kwargs) == expected
    assert Solution2().minWindow(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
