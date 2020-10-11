//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0210) {
    int row1[] = {1, 0};
    int *prerequisites[] = {row1};
    int prerequisitesSize = 1;
    int prerequisitesColSize[] = {2};
    int numCourses = 2;
    int returnSize = 2;
    int *res = findOrder(numCourses, prerequisites, prerequisitesSize, prerequisitesColSize, &returnSize);
//    printf("Res:%d", res[0]);
    int expected[] = {0, 1};
    ck_assert_uint_eq(sizeof(expected), sizeof(res));
    for (int i = 0; i < returnSize; ++i) {
        ck_assert_uint_eq(res[i], expected[i]);
    }
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0210");       // 建立Suite
    TCase *tc_add = tcase_create("t_0210");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0210);     // 测试用例加到测试集中
    return s;
}

