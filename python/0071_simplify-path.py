#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 13:40:50
# @Last Modified : 2020-04-25 13:40:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
#
#  在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成
# 部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
#
#  请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表
# 示绝对路径的最短字符串。
#
#
#
#  示例 1：
#
#  输入："/home/"
# 输出："/home"
# 解释：注意，最后一个目录名后面没有斜杠。
#
#
#  示例 2：
#
#  输入："/../"
# 输出："/"
# 解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
#
#
#  示例 3：
#
#  输入："/home//foo/"
# 输出："/home/foo"
# 解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
#
#
#  示例 4：
#
#  输入："/a/./b/../../c/"
# 输出："/c"
#
#
#  示例 5：
#
#  输入："/a/../../b/../c//.//"
# 输出："/c"
#
#
#  示例 6：
#
#  输入："/a//b////c/d//././/.."
# 输出："/a/b/c"
#  Related Topics 栈 字符串
#  👍 163 👎 0

"""

class Solution1:

    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        path_list = path.split("/")
        stack = []
        for i, w in enumerate(path_list):
            if not stack:
                stack.append("/")
            if stack[-1] != "/":
                stack.append("/")
            if not w:
                continue
            if w not in [".", ".."]:
                stack.append(w)
            elif w == ".." and len(stack) >= 2:
                stack.pop()
                stack.pop()
            elif w == ".":
                continue
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        return "".join(stack)


class Solution:

    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        path_list = path.split("/")
        stack = []
        for token in path_list:
            if token == ".." and stack:
                stack.pop()
            elif token and token not in [".", ".."]:
                stack.append(token)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "/...",
        "/home/",
        "",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
        "/a/../../b/../c//.//",
        "/a//b////c/d//././/..",
        "/a/../../b/../c//.//",
        "///eHx/.."
    ]
    res = [sol.simplifyPath(args) for args in samples]
    print(res)
