//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_1014)
    {
        int A[] = {8,1,5,2,6};
        int result = maxScoreSightseeingPair(A, sizeof(A) / sizeof(int));

        ck_assert_uint_eq( result,11);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_1014");       // 建立Suite
    TCase *tc_add = tcase_create("tt_1014");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_1014);     // 测试用例加到测试集中
    return s;
}
