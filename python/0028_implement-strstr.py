#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 20:48:11
# @Last Modified : 2020-04-08 20:48:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# Rabin Karp is OK

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        lennd = len(needle)
        if not lennd:return 0
        for i in range(len(haystack) - lennd + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

    def strStrKmp(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        return self.KMP(haystack, needle)

    def KMP(self, text, pattern):
        prefix = self.getPrefix(pattern)
        j = -1
        print(prefix)
        for i in range(len(text)):
            while j > -1 and pattern[j + 1] != text[i]:
                j = prefix[j]
            if pattern[j + 1] == text[i]:
                j += 1
            if j==len(pattern)-1:
                return  i-j
        return -1

    def getPrefix(self,pattern):
        lenP = len(pattern)
        prefixArray = [-1]* lenP
        j=-1
        for i in range(1,lenP):
            while j>-1 and pattern[j+1]!=pattern[i]:
                print(i,j,pattern[j],prefixArray[j])
                j = prefixArray[j]
            if pattern[j+1]==pattern[i]:
                j+=1
            prefixArray[i]=j
        return prefixArray



if __name__ == '__main__':
    sol = Solution()
    haystack = "helabalalaaballaalblacblaalaalalaabacbllalablaaao"
    needle = "laalblacblaalaa"
    # haystack = "a"*100000
    # needle = "a"*10000+"b"
    print(sol.strStrKmp(haystack, needle))
