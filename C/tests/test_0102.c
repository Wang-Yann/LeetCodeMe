//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_levelOrder) {
    //TODO TODO BUG
    struct TreeNode left = {1, NULL, NULL};
    struct TreeNode right = {3, NULL, NULL};
    struct TreeNode root = {2, &left, &right};


    int arr1[3];
    int arr2[3];
    int *ptr2[] = {arr1, arr2};
    int returnSize = 5;
    int **res = levelOrder(&root, &returnSize, ptr2);

    for (int i = 0; i < 2; ++i) {
        printf("Return: %d,%d\n", *res[i], *(res[i] + 1));
    }
    ck_assert(0 == memcmp(res, res, sizeof(res)));
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_levelOrder");       // 建立Suite
    TCase *tc_add = tcase_create("t_levelOrder");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_levelOrder);     // 测试用例加到测试集中
    return s;
}
