//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0221)
    {
        char *s1 = (char *) "10100";
        char *s2 = (char *)"10111";
        char *s3 = (char *)"11111";
        char *s4 = (char *) "10010";
//    char* matrix[] = {s1, s2, s3, s4};
    char *  matrix[] = {"10100", "10111", "11111", "10010"};
    int matrixCols[]={ 5,5,5,5};
    int res = maximalSquare(matrix, 4, matrixCols);
    printf("Res:%d\n", res);
    ck_assert_uint_eq(res, 4);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0221");       // 建立Suite
    TCase *tc_add = tcase_create("t_0221");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0221);     // 测试用例加到测试集中
    return s;
}
