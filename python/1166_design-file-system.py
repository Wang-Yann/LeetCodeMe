#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 10:59:47
# @Last Modified : 2020-08-05 10:59:47
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你需要设计一个能提供下面两个函数的文件系统： 
# 
#  
#  create(path, value): 创建一个新的路径，并尽可能将值 value 与路径 path 关联，然后返回 True。如果路径已经存在或者路径
# 的父路径不存在，则返回 False。 
#  get(path): 返回与路径关联的值。如果路径不存在，则返回 -1。 
#  
# 
#  “路径” 是由一个或多个符合下述格式的字符串连接起来形成的：在 / 后跟着一个或多个小写英文字母。 
# 
#  例如 /leetcode 和 /leetcode/problems 都是有效的路径，但空字符串和 / 不是有效的路径。 
# 
#  好了，接下来就请你来实现这两个函数吧！（请参考示例以获得更多信息） 
# 
#  
# 
#  示例 1： 
# 
#  输入： 
# ["FileSystem","create","get"]
# [[],["/a",1],["/a"]]
# 输出： 
# [null,true,1]
# 解释： 
# FileSystem fileSystem = new FileSystem();
# 
# fileSystem.create("/a", 1); // 返回 true
# fileSystem.get("/a"); // 返回 1
#  
# 
#  示例 2： 
# 
#  输入： 
# ["FileSystem","create","create","get","create","get"]
# [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
# 输出： 
# [null,true,true,2,false,-1]
# 解释：
# FileSystem fileSystem = new FileSystem();
# 
# fileSystem.create("/leet", 1); // 返回 true
# fileSystem.create("/leet/code", 2); // 返回 true
# fileSystem.get("/leet/code"); // 返回 2
# fileSystem.create("/c/d", 1); // 返回 false 因为父路径 "/c" 不存在。
# fileSystem.get("/c"); // 返回 -1 因为该路径不存在。
#  
# 
#  
# 
#  提示： 
# 
#  
#  对两个函数的调用次数加起来小于等于 10^4 
#  2 <= path.length <= 100 
#  1 <= value <= 10^9 
#  
#  Related Topics 设计 哈希表 
#  👍 7 👎 0

"""

import pytest
from sample_datas import BIG_1166


# leetcode submit region begin(Prohibit modification and deletion)


class FileSystem:
    """题目测试用例有问题？　没问题"""

    def __init__(self):
        self.lookup = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        if path in ("", "/"):
            return False
        path = path.strip("/")
        # 下面的大测试用例一直过不了是因为这里写错了,写成了"".join ^_^　
        prefix = "/".join(path.split("/")[:-1])
        if prefix not in self.lookup or path in self.lookup:
            return False
        self.lookup[path] = value
        return True

        # if path[:path.rfind('/')] not in self.lookup or path in self.lookup:
        #     return False
        # self.lookup[path] = value
        # return True

    def get(self, path: str) -> int:
        path = path.strip("/")
        return self.lookup.get(path, -1)
        # return self.lookup.get(path, -1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    fileSystem = FileSystem()
    assert fileSystem.createPath("/leet", 1)
    assert fileSystem.createPath("/leet/code", 2)
    assert fileSystem.get("/leet/code") == 2
    assert fileSystem.createPath("/c/d", 1) == False  # // 返回 false 因为父路径 "/c" 不存在。
    assert fileSystem.get("/c") == -1  # // 返回 -1 因为该路径不存在。


def test_solution_case():
    obj = FileSystem()
    for method, args, expected in zip(BIG_1166.BIG_INPUT[1:],
                                      BIG_1166.BIG_ARGS[1:],
                                      BIG_1166.BIG_EXPECTED[1:]):
        res = getattr(obj, method)(*args)
        if res != expected:
            print(method, args, expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
