#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-06 21:02:06
# @Last Modified : 2020-04-06 21:02:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


class Solution:
    """
    i是截至j，以j为最后一个元素的最长不重复子串的起始位置，即索引范围是[i,j]的子串是以索引j为最后一个元素的最长子串。 当索引从j-1增加到j时，原来的子串[i,j-1]新增了一个元素变为[i,j]，需要判断j是否与[i,j-1]中元素有重复。所以if s[j] in st:是判断s[j]相同元素上次出现的位置，和i孰大孰小。如果i大，说明[i,j-1]中没有与s[j]相同的元素，起始位置仍取i；如果i小，则在[i,j-1]中有了与s[j]相同的元素，所以起始位置变为st[s[j]]+1，即[st[sj]+1,j]。而省略掉的else部分，由于s[j]是第一次出现所以前面必然没有重复的，仍然用i作为起始位置即可。 后面的ans=max(ans,j-i+1)中，括号中前者ans是前j-1个元素最长子串长度，j-i+1是以s[j]结尾的最长子串长度，两者（最长子串要么不包括j，要么包括j）取最大即可更新ans，遍历所有i后得到整个输入的最长子串长度
    """

    def lengthOfLongestSubstring0(self, s: str) -> int:
        if not s:
            return 0
        left, result = 0, 0
        lookup = {}
        # left是截至right，以right为最后一个元素的最长不重复子串的起始位置
        # 即索引范围是[left,right]的子串是以索引j为最后一个元素的最长子串
        for right in range(len(s)):
            print(lookup, right, left, result)
            if s[right] in lookup:
                left = max(left, lookup[s[right]] + 1)
            lookup[s[right]] = right
            result = max(result, right - left + 1)
            # 括号中前者ans是前j-1个元素最长子串长度，j-i+1是以s[j]结尾的最长子串长度
        return result

    def lengthOfLongestSubstring(self, s: str) -> int:
        """https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetcod/
        滑动窗口是数组/字符串问题中常用的抽象概念。 窗口通常是在数组/字符串中由开始和结束索引定义的一系列元素的集合，即 [i, j)[i,j)（左闭，右开）"""
        if not s:
            return 0
        length = len(s)
        st = set()
        result, i, j = 0, 0, 0
        while i < length and j < length:
            if s[j] not in st:
                st.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                st.remove(s[i])
                i += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    sample = "ppwwkew"
    print(sol.lengthOfLongestSubstring(sample))
