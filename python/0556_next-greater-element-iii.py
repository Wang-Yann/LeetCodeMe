#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-26 15:37:23
# @Last Modified : 2020-04-26 15:37:23
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
#
#  示例 1:
#
#
# 输入: 12
# 输出: 21
#
#
#  示例 2:
#
#
# 输入: 21
# 输出: -1
#
#  Related Topics 字符串
#  👍 79 👎 0

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        TODO
        """
        digits = list(map(int,list(str(n))))
        k,l=-1,0
        length = len(digits)
        #左边升序
        for i in range(length-1):
            if digits[i]<digits[i+1]:
                k=i
        if k==-1:
            digits.reverse()
            return -1
        for i in range(k+1,length):
            if digits[i]>digits[k]:
                l=i
        print("k-l:",k,l,digits)
        digits[l],digits[k] = digits[k],digits[l]
        digits[k+1:]=digits[length-1:k:-1]
        result= int("".join(map(str,digits)))
        return -1 if result>0x7FFFFFFF else result



if __name__ == '__main__':
    sol = Solution()
    samples = [
        12,  143256 ,103 ,
        123654776

    ]
    lists = [x for x in samples]
    res = [sol.nextGreaterElement(x) for x in lists]
    print(res)
