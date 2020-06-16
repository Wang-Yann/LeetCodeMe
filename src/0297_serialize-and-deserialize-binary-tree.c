//
/* Created by rock on 6/16/20.
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/** Encodes a tree to a single string. */
#include "leetcode_functions.h"

#define MAX_SIZE 100000
#define STR_SIZE 10

void pre_order(struct TreeNode *root, char *data) {
    if (root == NULL) {
        strcat(data, "#");
        strcat(data, ",");
        return;
    }
    char tmp[STR_SIZE] = "";
    sprintf(tmp, "%d", root->val);
    strcat(data, tmp);
    strcat(data, ",");
    pre_order(root->left, data);
    pre_order(root->right, data);

}

struct TreeNode *createTree(char *data, int *index) {
    if (data[*index] == '#') {
        (*index)++; //#
        (*index)++; //,
        return NULL;
    }
    struct TreeNode *root = malloc(sizeof(struct TreeNode));
    char tmp[STR_SIZE] = "";
    int k = 0;
    while (data[*index] != ',') {
        tmp[k++] = data[*index];
        (*index)++;
    }
    (*index)++;

    root->val = atoi(tmp);
    root->left = createTree(data, index);
    root->right = createTree(data, index);
    return root;
}

char *serialize(struct TreeNode *root) {
    char *ans = malloc(sizeof(char) * MAX_SIZE);
    memset(ans, '\0', sizeof(char) * MAX_SIZE);
    pre_order(root, ans);
    return ans;

}

/** Decodes your encoded data to tree. */
struct TreeNode *deserialize(char *data) {
    int index = 0;
    return createTree(data, &index);

}

// Your functions will be called as such:
// char* data = serialize(root);
// deserialize(data);

int main(int argc, char **argv) {
    struct TreeNode left = {1, NULL, NULL};
    struct TreeNode right = {3, NULL, NULL};
    struct TreeNode root = {2, &left, &right};
    char *s = serialize(&root);
    printf("%s\n", s);
    struct TreeNode *expected = malloc(sizeof(struct TreeNode));
    expected = deserialize(s);
    assert(expected->val == root.val);
    assert(expected->left->val == root.left->val);
    assert(expected->right->val == root.right->val);
    return 0;

}