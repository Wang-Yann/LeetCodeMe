#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 20:57:45
# @Last Modified : 2020-04-26 20:57:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0
import collections
import re


class Solution0:

    def countOfAtoms(self, formula: str) -> str:
        """
        官方解法 HARD
        """
        N = len(formula)
        idx = 0
        ans = []

        def parseRecu():
            nonlocal idx
            count = collections.Counter()
            while idx < N and formula[idx] != ")":
                if formula[idx] == "(":
                    idx += 1
                    for name, v in parseRecu().items():
                        count[name] += v
                else:
                    i_start = idx
                    idx += 1
                    while idx < N and formula[idx].islower():
                        idx += 1
                    name = formula[i_start:idx]
                    i_start = idx
                    while idx < N and formula[idx].isdigit():
                        idx += 1
                    count[name] += int(formula[i_start:idx] or 1)
            idx += 1
            i_start = idx
            while idx < N and formula[idx].isdigit():
                idx += 1
            if i_start < idx:
                multi_times = int(formula[i_start:idx])
                for name in count:
                    # print("count",name,multi_times)
                    count[name] *= multi_times
            # print("[]",formula,count)
            return count

        counter = parseRecu()
        for name_key in sorted(counter):
            ans.append(name_key)
            times = counter[name_key]
            if times > 1:
                ans.append(str(times))
        return "".join(ans)


class Solution:

    def countOfAtoms(self, formula: str) -> str:
        """
        官方解法 正则
        """
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
                stack[-1][name] += int(m1 or 1)
            if left_open:
                stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                    stack[-1][k] += top[k] * int(m2 or 1)
        return "".join(
            name + (str(stack[-1][name]) if stack[-1][name] > 1 else "")
            for name in sorted(stack[-1])
        )


if __name__ == '__main__':
    sol = Solution()
    samples = [
        "H2O",
        "Mg(OH)2",
        "K4(ON(SO3)2)2"

    ]
    res = [sol.countOfAtoms(args) for args in samples]
    print(res)
