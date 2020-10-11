//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(spiralOrder_test)
    {
        int m[3][3] = {{1, 2, 3},
                       {4, 5, 6},
                       {7, 8, 9}};
        int *matrix[3];
        for (int i = 0; i < 3; i++) {
            matrix[i] = m[i];
        }
        int matrixSize = 3;
        int matrixColSize[] = {3, 3, 3};
        int returnSize;
        int expected[] = {1, 2, 3, 6, 9, 8, 7, 4, 5};
        int *res = spiralOrder(matrix, matrixSize, matrixColSize, &returnSize);
        ck_assert_double_eq_tol(returnSize, matrixSize * matrixColSize[0], ELLIPSIS);
        for (int i = 0; i < returnSize; ++i) {
            ck_assert_double_eq_tol(*(res + i), expected[i],ELLIPSIS);
        }
    }

END_TEST

Suite *make_a_suite(void) {
    Suite *s = suite_create("spiralOrder_test");       // 建立Suite
    TCase *tc_add = tcase_create("spiralOrder_test");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, spiralOrder_test);     // 测试用例加到测试集中
    return s;
}
