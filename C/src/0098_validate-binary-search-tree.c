//
/* Created by rock on 5/4/20.
*/

#include "leetcode_functions.h"

bool isValidRecu(struct TreeNode *root, long low, long high) {
    if (root == NULL) {
        return true;
    }

    return low < root->val && root->val < high
           && isValidRecu(root->left, low, root->val)
           && isValidRecu(root->right, root->val, high);
};

bool isValidBST(struct TreeNode * root) {

    return isValidRecu(root, LONG_MIN, LONG_MAX);

}
