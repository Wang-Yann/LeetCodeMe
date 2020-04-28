#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-10 21:44:06
# @Last Modified : 2020-04-10 21:44:06
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback



class Solution:
    def reverseWords(self, s: str) -> str:
        if not s.strip():return ""
        s_list = s.strip().split(" ")
        return " ".join(w.strip(" ")  for w in s_list[::-1] if w)




if __name__ == '__main__':
    sol = Solution()
    sample="the sky is blue"
    sample="  hello world! "
    sample="a good   example"
    print(sol.reverseWords(sample))





























