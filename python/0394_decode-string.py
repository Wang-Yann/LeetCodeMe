#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 10:57:44
# @Last Modified : 2020-04-26 10:57:44
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


class Solution0:
    def decodeString(self, s: str) -> str:
        """
        TODO
        """
        stack, res, times = [], "", 0
        for c in s:
            if c == "[":
                stack.append([times, res])
                res, times = "", 0
            elif c == "]":
                cur_times, last_res = stack.pop()
                res = last_res + cur_times * res
            elif "0" <= c <= "9":
                times = times * 10 + ord(c) - ord("0")
            else:
                res += c
        return res


class Solution:
    def decodeString(self, s: str) -> str:
        times_stack = []
        str_stack = []

        num, cur = 0, ""
        i = 0
        length = len(s)
        while i <= length - 1:
            if s[i] == "[":
                times_stack.append(num)
                str_stack.append(cur)
                num = 0
                cur = ""
                i += 1
            elif s[i].isalpha():
                j = i + 1
                while j <= length - 1 and s[j].isalpha():
                    j += 1
                cur += s[i:j]
                i = j
            elif s[i].isdigit():
                j = i + 1
                while j <= length - 1 and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j
            elif s[i] == "]":
                times = times_stack.pop()
                last = str_stack.pop()
                cur = last + cur * times
                i += 1
        return cur


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "3[a]2[b4[F]c]",  # "aaabFFFFcbFFFFc"
        "3[a]2[bc]",
        "3[a2[c]]",
        "3[a2[c1[ee]]]",
        "2[abc]3[cd]ef"
    ]
    lists = [x for x in samples]
    res = [sol.decodeString(x) for x in lists]
    print(res)
