//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_1431) {
    int candies[] = {2, 3, 5, 1, 3};
    int candiesSize = sizeof(candies) / sizeof(int);
    int extraCandies = 3;
    int returnSize;
    bool expected[] = {true, true, true, false, true};
    bool *res = kidsWithCandies(candies, candiesSize, extraCandies, &returnSize);
//        sleep(30);
    ck_assert_uint_eq(returnSize, candiesSize);
//    ck_assert_uint_eq(sizeof(expected), sizeof(res));
    for (int i = 0; i < returnSize; ++i) {
        ck_assert_uint_eq(res[i], expected[i]);
    }
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_1431");       // 建立Suite
    TCase *tc_add = tcase_create("tt_1431");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_1431);     // 测试用例加到测试集中
    return s;
}
