//
/* Created by rock on 6/21/20.
*/
#include "leetcode_functions.h"

int maxPathGain(TreeNode *node, int *maxValue) {
    if (node == NULL) {
        return 0;
    }
    int leftGain = fmax(maxPathGain(node->left,maxValue), 0);
    int rigthGain = fmax(maxPathGain(node->right,maxValue), 0);

    int priceNew = leftGain + rigthGain + node->val;

    *maxValue = fmax(*maxValue, priceNew);
    return node->val + fmax(leftGain, rigthGain);

}

int maxPathSum(struct TreeNode *root) {
    int maxValue = INT_MIN;
    maxPathGain(root, &maxValue);
    return maxValue;


}