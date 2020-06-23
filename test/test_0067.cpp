//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(addBinary, test1) {
    char a[] = "11";
    char b[] = "1";
    char *res1 = addBinary(a, b);
    char exp1[] = "100";
    printf("Res1:%s\n", res1);
    ASSERT_TRUE(strcmp(res1, exp1) == 0);
}

TEST(addBinary, test2) {
    char a[] = "1010";
    char b[] = "1011";
    ASSERT_TRUE(strcmp(addBinary(a, b), "10101") == 0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}