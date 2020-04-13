#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 23:14:19
# @Last Modified : 2020-04-10 23:14:19
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s =str(x)
        l =0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def isPalindromeS(self, x):
        if x < 0:
            return False
        copy, reverse = x, 0

        while copy:
            reverse *= 10
            reverse += copy % 10
            copy //= 10

        return x == reverse



if __name__ == '__main__':
    sol = Solution()
    sample=[121,10,-1,1,11,0,1234,1221,434]
    print([sol.isPalindrome(x) for x in sample] )


