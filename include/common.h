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


#define max(a, b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; });


#define min(a, b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

#define MIN(a, b, c) ((a)<(b)?( (a)<(c)?(a):(c) ):( (b)<(c)?(b):(c) ))

typedef struct ListNode ListNode;
typedef struct TreeNode TreeNode;

struct ListNode {
    int val;
    struct ListNode *next;
};

ListNode *initNodeList(int *nums, int size);

bool checkListEqual(ListNode *res, ListNode *expected);


struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};


#endif //LEETCODE_COMMON_H
