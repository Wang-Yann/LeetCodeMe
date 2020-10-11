//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_buildTree) {
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
//    ck_assert(checkTreeEqual(res, res));
    ck_assert(checkTreeEqual(res, &root));
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_buildTree");       // 建立Suite
    TCase *tc_add = tcase_create("t_buildTree");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_buildTree);     // 测试用例加到测试集中
    return s;
}
