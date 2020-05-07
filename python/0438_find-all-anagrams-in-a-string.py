#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表

https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/
"""
import collections
from typing import List

import pytest




# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    /* 滑动窗口算法框架 */
    void slidingWindow(string s, string t) {
        unordered_map<char, int> need, window;
        for (char c : t) need[c]++;

        int left = 0, right = 0;
        int valid = 0;
        while (right < s.size()) {
            // c 是将移入窗口的字符
            char c = s[right];
            // 右移窗口
            right++;
            // 进行窗口内数据的一系列更新
            ...

            /*** debug 输出的位置 ***/
            printf("window: [%d, %d)\n", left, right);
            /********************/

            // 判断左侧窗口是否要收缩
            while (window needs shrink) {
                // d 是将移出窗口的字符
                char d = s[left];
                // 左移窗口
                left++;
                // 进行窗口内数据的一系列更新
                ...
            }
        }
    }

    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Good"""
        result = []
        cnts = collections.Counter(p)
        left, right = 0, 0
        while right < len(s):
            cnts[s[right]] -= 1
            # print("window: [%d, %d)" %(left, right),cnts)
            while left <= right and cnts[s[right]] < 0:
                cnts[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                result.append(left)
            right += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """超时"""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        res = []
        key = sorted(p)
        for i in range(0, len_s - len_p + 1):
            if s[i] in key:
                if sorted(s[i:i + len_p]) == key:
                    res.append(i)
            i += 1
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(s="cbaebabacd", p="abc"), [0, 6]],
    # [dict(s="abab", p="ab"), [0, 1, 2]],
])
def test_solutions(kw, expected):
    assert Solution().findAnagrams(**kw) == expected
    # assert Solution1().findAnagrams(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
