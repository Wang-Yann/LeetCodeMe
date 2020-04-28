#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 22:40:42
# @Last Modified : 2020-04-10 22:40:42
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback


class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        flag = -1 if x<0 else 1
        x = flag*x
        INT_MAX=2**31-1
        INT_HEAD,MIN_LAST,MAX_LAST = INT_MAX//10,8,7
        while x!=0:
            v= x%10
            x = x//10
            if num>INT_HEAD  or (
                num==INT_HEAD and (flag ==-1 and v>MIN_LAST or flag==1 and v>MAX_LAST)
            ):
                return 0
            num=num*10+v

        return num*flag




if __name__ == '__main__':
    sol = Solution()
    sample=-123
    sample1=120
    sample1=2**31+1
    sample1=2**31//10
    print(sol.reverse(sample))
    print(sol.reverse(sample1))



