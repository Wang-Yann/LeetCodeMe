#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 17:27:58
# @Last Modified : 2020-04-26 17:27:58
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

class Solution:
    def isValid(self, code: str) -> bool:
        """
        HARD
        """
        def validText(s, i):
            j = i
            i = s.find("<", i)
            return i != j, i

        def validCData(s, i):
            if s.find("<![CDATA[", i) != i:
                return False, i
            j = s.find("]]>", i)
            if j == -1:
                return False, i
            return True, j + 3

        def parseTagName(s, i):
            if s[i] != "<":
                return "", i
            j = s.find(">", i)
            if j == -1 or not (1 <= (j - 1 - i) <= 9):
                return "", i
            tag = s[i + 1:j]
            for c in tag:
                if not ord("A") <= ord(c) <= ord("Z"):
                    return "", i
            return tag, j + 1

        def validTag(s, i):
            tag, j = parseTagName(s, i)
            if not tag:
                return False, i
            j = parseContent(s, j)
            k = j + len(tag) + 2
            if k >= len(s) or s[j:k + 1] != "</" + tag + ">":
                return False, i
            return True, k + 1

        def parseContent(s, i):
            while i < len(s):
                result, i = validText(s, i)
                if result:
                    continue
                result, i = validCData(s, i)
                if result:
                    continue
                result, i = validTag(s, i)
                if result:
                    continue
                break
            return i

        result, i = validTag(code, 0)
        return result and i == len(code)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "<DIV>This is the first line <![CDATA[<div>]]></DIV>",
        "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>",
        "<A>  <B> </A>   </B>",
        "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>",
        "<DIV>  unmatched <  </DIV>"

    ]
    lists = [x for x in samples]
    res = [sol.isValid(x) for x in lists]
    print(res)
