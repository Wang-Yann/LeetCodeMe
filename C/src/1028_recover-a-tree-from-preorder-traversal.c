//
/* Created by rock on 6/18/20.
*/

#include "leetcode_functions.h"


struct TreeNode *helper(char **S, int depth) {
    int flagCnt = 0;
    char *head = *S;
    while (*head == '-') {
        flagCnt++;
        head++;
    }
    if (flagCnt != depth) {
        return NULL;
    }

    *S = head;
    int num = 0;
    while (**S != '-' && **S != '\0') {
        num = 10 * num + *((*S)++) - '0';
    }
    struct TreeNode *node = (struct TreeNode *) malloc(sizeof(struct TreeNode));
    node->val = num;
    // printf("深度：%d,value:%d, 剩余字符：%s\n",depth,num, *S);
    node->left = helper(S, depth + 1);
    // printf("（左边赋值）剩余字符：%s\n",*S);
    node->right = helper(S, depth + 1);
    // printf("（右边赋值剩余字符：%s\n", *S);
    return node;
}

struct TreeNode *recoverFromPreorder(char *S) {
    if (strlen(S) == 0) {
        return NULL;
    }
    return helper(&S, 0);
}