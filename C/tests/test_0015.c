//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_threeSum) {
    int nums[] = {-1, 0, 1, 2, -1, -4};
    int numSize = 6;
    int returnSize;
    int **returnColumnSizes = (int **) malloc(sizeof(int *) * 6);;
    int **res;

    int arr1[] = {-1, -1, 2};
    int arr2[] = {-1, 0, 1};
    int *expected[] = {arr1, arr2};
    res = threeSum(nums, numSize, &returnSize, returnColumnSizes);

    ck_assert_uint_eq(returnSize, 2);
    for (int i = 0; i < returnSize; i++) {
        int columnSize = (*returnColumnSizes)[i];
        ck_assert_uint_eq(columnSize, 3);
        for (int j = 0; j < columnSize; j++) {
            printf("Return: %d\n", res[i][j]);
            ck_assert_uint_eq(res[i][j], expected[i][j]);
        }
    }
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_threeSum");       // 建立Suite
    TCase *tc_add = tcase_create("t_threeSum");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_threeSum);     // 测试用例加到测试集中
    return s;
}
