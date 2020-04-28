#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-25 13:40:50
# @Last Modified : 2020-04-25 13:40:50
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


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
