//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0236) {
    struct TreeNode left = {
            .val=1,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode right = {
            .val=3,
            .left=NULL,
            .right=NULL
    };
    struct TreeNode root = {
            val:2,
            left:&left,
            right:&right,
    };
    struct TreeNode *res = lowestCommonAncestor(&root, &left, &right);
    ck_assert_uint_eq(res->val, root.val);
}
//
//TEST(lowestCommonAncestor, test1) {
//struct TreeNode left = {1, NULL, NULL};
//struct TreeNode right = {3, NULL, NULL};
//struct TreeNode root = {2, &left, &right};
//struct TreeNode *res = lowestCommonAncestor(&root, &left, &right);
//ck_assert_uint_eq(res, &root);

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0236");       // 建立Suite
    TCase *tc_add = tcase_create("t_0236");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0236);     // 测试用例加到测试集中
    return s;
}


