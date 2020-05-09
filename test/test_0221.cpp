//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(maximalSquareTest, test1) {
    char *s1 = (char *) "10100";
    char *s2 = (char *)"10111";
    char *s3 = (char *)"11111";
    char *s4 = (char *) "10010";
//    char* matrix[] = {s1, s2, s3, s4};
    char *  matrix[] = {"10100", "10111", "11111", "10010"};
    int matrixCols[]={ 5,5,5,5};
    int res = maximalSquare(matrix, 4, matrixCols);
    printf("Res:%d\n", res);
    ASSERT_EQ(res, 4);
}

//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}
