//
/* Created by rock on 5/13/20.
*/

#include "leetcode_functions.h"

#define MAXSIZE 1000
#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; });
int **levelOrder(struct TreeNode *root, int *returnSize, int **returnColumnSizes) {
    *returnSize = 0;
    if (root == NULL) {
        return NULL;
    }

    returnColumnSizes[0] = (int *) calloc(MAXSIZE, sizeof(int));
    int **res = (int **) malloc(sizeof(int *) * MAXSIZE);
    void dfs(struct TreeNode *root, int level) {
        if (root == NULL) {
            *returnSize = max(*returnSize, level);
            return;
        }
        dfs(root->left, level + 1);
        dfs(root->right, level + 1);

        if (returnColumnSizes[0][level] == NULL) {
            res[level] = (int *) calloc(MAXSIZE, sizeof(int));
        }
        res[level][returnColumnSizes[0][level]++] = root->val;
        return;
    }


    dfs(root, 0);
    return res;

}