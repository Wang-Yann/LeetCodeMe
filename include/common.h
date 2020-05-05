#pragma  once
#ifndef LEETCODE_COMMON_H
#define LEETCODE_COMMON_H

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdarg.h>
#include <assert.h>
#include <ctype.h>
#include <time.h>
#include <float.h>
#include <errno.h>
#include <limits.h>


struct ListNode {
    int val;
    struct ListNode *next;
};
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

#endif //LEETCODE_COMMON_H
