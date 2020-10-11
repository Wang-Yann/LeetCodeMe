//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_isValidBST1)
    {
        struct TreeNode left = {1, NULL, NULL};
        struct TreeNode right = {3, NULL, NULL};
        struct TreeNode root = {2, &left, &right};
        ck_assert_msg(isValidBST(&root), "Part1");
    }
END_TEST

START_TEST(t_isValidBST2)

    {
        struct TreeNode left = {1, NULL, NULL};
        struct TreeNode right = {1, NULL, NULL};
        right.val = 3;
        struct TreeNode root = {100, &left, &right};
        ck_assert_msg(isValidBST(&root), "Part2");
    }
END_TEST

START_TEST(t_isValidBST3)

    {
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
        ck_assert_msg(isValidBST(&root), "Part3");
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_isValidBST");       // 建立Suite
    TCase *tc_add = tcase_create("t_isValidBST");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_isValidBST1);     // 测试用例加到测试集中
    tcase_add_test(tc_add, t_isValidBST2);     // 测试用例加到测试集中
    tcase_add_test(tc_add, t_isValidBST3);     // 测试用例加到测试集中
    return s;
}

