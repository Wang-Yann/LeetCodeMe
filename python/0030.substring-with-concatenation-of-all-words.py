#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-08 22:01:25
# @Last Modified : 2020-04-08 22:01:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import os
import sys
import traceback
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not (s and words):return []
        res = []
        words.sort()
        lws,ls = len(words),len(s)
        lw = len(words[0])
        for i in range(ls-lw*lws+1):
            if self.checkExistAll(words,s[i:i+lw*lws],lws,lw):
                res.append(i)
        return res

    def checkExistAll(self,words,s,lws,lw):
        tmp_list =[]
        for i in range(lws):
            word = s[i*lw:(i+1)*lw]
            if word in words:
                tmp_list.append(word)
            else:
                return False

        return sorted(tmp_list)==words






if __name__ == '__main__':
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(sol.findSubstring(s,words))

