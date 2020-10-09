//
/* Created by rock on 5/4/20.
*/

#include "leetcode_functions.h"

bool isSymmetricRecu(struct TreeNode *left, struct TreeNode *right) {
    if (left == NULL && right == NULL) {
        return true;
    }
    if (left != NULL && right != NULL) {
        return left->val == right->val
               && isSymmetricRecu(left->left, right->right)
               && isSymmetricRecu(left->right, right->left);
    }

    return false;
};

bool isSymmetric(struct TreeNode *root) {
    if (root == NULL) {
        return true;
    }
    return isSymmetricRecu(root->left, root->right);

}
