#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 15:52:05
# @Last Modified : 2020-07-30 15:52:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 对于一个压缩字符串，设计一个数据结构，它支持如下两种操作： next 和 hasNext。 
# 
#  给定的压缩字符串格式为：每个字母后面紧跟一个正整数，这个整数表示该字母在解压后的字符串里连续出现的次数。 
# 
#  next() - 如果压缩字符串仍然有字母未被解压，则返回下一个字母，否则返回一个空格。 
# hasNext() - 判断是否还有字母仍然没被解压。 
# 
#  注意： 
# 
#  请记得将你的类在 StringIterator 中 初始化 ，因为静态变量或类变量在多组测试数据中不会被自动清空。更多细节请访问 这里 。 
# 
#  示例： 
# 
#  StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
# 
# iterator.next(); // 返回 'L'
# iterator.next(); // 返回 'e'
# iterator.next(); // 返回 'e'
# iterator.next(); // 返回 't'
# iterator.next(); // 返回 'C'
# iterator.next(); // 返回 'o'
# iterator.next(); // 返回 'd'
# iterator.hasNext(); // 返回 true
# iterator.next(); // 返回 'e'
# iterator.hasNext(); // 返回 false
# iterator.next(); // 返回 ' '
#  
# 
#  
#  Related Topics 设计 
#  👍 17 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class StringIterator:

    def __init__(self, compressedString: str):
        self.data = []
        char = ""
        cnt = 0
        for i in range(len(compressedString)):
            if compressedString[i].isdigit():
                cnt = 10 * cnt + int(compressedString[i])
            else:
                if cnt:
                    self.data.append([char, cnt])
                char = compressedString[i]
                cnt = 0
        self.data.append([char, cnt])

    def next(self) -> str:
        if self.data:
            char, cnt = self.data[0]
            if cnt == 1:
                self.data.pop(0)
            else:
                self.data[0][1] -= 1
            return char
        return " "

    def hasNext(self) -> bool:
        return bool(self.data)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    # """L10e2t1C1o1d1e11"""
    iterator = StringIterator("L1e2t1C1o1d1e1")
    assert iterator.next() == 'L'
    assert iterator.next() == 'e'
    assert iterator.next() == 'e'
    assert iterator.next() == 't'
    assert iterator.next() == 'C'
    assert iterator.next() == 'o'
    assert iterator.next() == 'd'
    assert iterator.hasNext() == True
    assert iterator.next() == 'e'
    assert iterator.hasNext() == False
    assert iterator.next() == ' '


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
