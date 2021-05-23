#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-30 14:01:39
# @Last Modified : 2021-03-30 14:56:22
# @Mail          : lostlorder@gamil.com
import collections
import os
import re

import pytest


# ------------------------------------

def fizzbuzz(lst):
    """
    The Problem is go through all numbers in input list.
    If the number divisible by three is replaced by the word 'fizz'
    and any divisible by five by the word 'buzz'.
    Numbers divisible by both become 'fizzbuzz'.
    Example
    -------
    Input lst: [1, 3, 5, 7, 9, 11, 13, 15]
    Output: [1, 'fizz', 'buzz', 7, 'fizz', 11, 13, 'fizzbuzz']
    Parameter
    ---------
    lst: list
    list of integers
    Return
    ------
    list
    Be replaced new list.
    """
    assert isinstance(lst, list)
    ans = []
    for num in lst:
        if num % 15 == 0:
            ans.append("fizzbuzz")
        elif num % 3 == 0:
            ans.append("fizz")
        elif num % 5 == 0:
            ans.append("buzz")
        else:
            ans.append(num)
    return ans


# ------------------------------------


def moving_back(moves):
    """
    The problem is that you need to consider a robot
    that can be given an input string in the form
    of U, D, L, R - Move Up, Move Down, Move Left, Move Right.

    For instance: `UULL`
    L L
    end pos 一一
    | U
    | U
    start position
    If the robot starts at the origin (0,0), each input
    moves the robot in the given direction by 1 meter.
    So if input is 'UUL', the robot will move up by 2
    meters and then move to left 1 meter.
    Simialrly if input is 'UD' or 'LR' the robot will
    be back in the origin.
    The problem is that for a given input string of
    movements, you need to determine if the robot is
    back in the origin or not.
    Parameter
    ---------
    str: moves
    A list of movements, only contains 'U','D','L','R'
    Return
    ------
    bool
    Whether robot back to starting position.

    Example
    -------
    >>> moving_back('UU')
    False
    >>> moving_back('UDLR')
    True
    """
    # Your code here
    counter = collections.Counter(moves)
    return counter["L"] == counter["R"] and counter["U"] == counter["D"]


# ----------------------------------
#
# There is a SQL table score which contains student_id , course_id and course_score .
# Please write SQL to return top1 student_id and total course_score who has highest total score of all courses.
# Tabel example:

# SQL

""" 
    select student_id as student_id,sum(course_score)  as course_score from  student_scores group by student_id order by sum(course_score) desc limit 1

"""


# ------------------------------------

#
#
# Write a program that reads a text file from the same directory that your main program is stored and then
# perform some operations on it. Concretely:
# 1. Your program reads from the console (1) the name of the file (“test.txt” for instance) and (2) an integer k.
# 2. Your program then reads the file. While reading the file (NOT after the file has been read), you need to
# count the occurrence of each word. Note that “cat” and “cats” could be considered as two different words.
# In addition, special characters such as ./*? are all separate words. For instance, “I’m having some
# headache” has six words [“I”, “‘”, “m”, “having”, “some”, “headache”].
# 3. Once the file-reading is completed, your program should output the EXACT (not approximate) the top k
# most frequent words. In case there are ties in terms of word frequencies, return all


def process_and_output_top_k_words(filename, k):
    """
    TODO Which are all special Characters?
    TODO output words with same frequences?            
    :param filename:ilename for process words
    :param k: top k settings
    :return: top k frequeceny words
    """
    counter = collections.Counter()
    pat = re.compile(r"[./?\s\t\n\r\f\v]+")
    SPECIAL_WORD_CHAR = "’"
    with open(filename, "r") as f:
        for line in f.readlines():
            for word in pat.split(line.strip()):
                if SPECIAL_WORD_CHAR in word:
                    parts = word.split(SPECIAL_WORD_CHAR)
                    counter.update(parts)
                    counter.update(SPECIAL_WORD_CHAR)
                else:
                    counter[word] += 1
    most_cnts = set(sorted(set(counter.values()), reverse=True)[:k])
    ans = []
    for x in counter.most_common():
        if x[1] in most_cnts:
            ans.append(x[0])
        else:
            break
    return ans


def read_file_prompt():
    """
    CMD line
    :return:
    """
    name = input("input Filename?\n")
    k = input("input number K?\n")
    assert os.path.isfile(name)
    res = process_and_output_top_k_words(name, k)
    print(res)


# ----TESTS---


def test_fizzbuzz():
    assert fizzbuzz([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 'fizz', 'buzz', 7, 'fizz', 11, 13, 'fizzbuzz']


@pytest.mark.parametrize("args,expected", [
    ("UU", False),
    ("UDLR", True),
])
def test_solutions(args, expected):
    assert moving_back(args) == expected


def test_process_and_output_top_k_words():
    assert sorted(process_and_output_top_k_words("test.txt", 1)) == sorted(['Hello', 'World'])


if __name__ == '__main__':
    # pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
    read_file_prompt()
