//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(buildTree, test3) {
    struct TreeNode t15 = {
            .val=15,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t7 = {
            .val=7,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode t20 = {
            .val=20,
            .left = &t15,
            .right=&t7
    };
    struct TreeNode t9 = {
            9, NULL, NULL
    };
    struct TreeNode root = {3, &t9, &t20};

    int preorder[] = {3, 9, 20, 15, 7};
    int inorder[] = {9, 3, 15, 20, 7};
    int preOrderSize = sizeof(preorder) / sizeof(int);
    int inorderSize = sizeof(inorder) / sizeof(int);

    struct TreeNode *res = buildTree(preorder, preOrderSize, inorder, inorderSize);
//    ASSERT_TRUE(checkTreeEqual(res, res));
    ASSERT_TRUE(checkTreeEqual(res, &root));

}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
