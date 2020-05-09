//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
#include "test_common.cpp"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(isNumber, test1) {
    char s1[]= " -90e3   ";
    char s2[]= "e3";
    char s3[] = "53.5e93";
    char s4[] = "95a54e53";
    char s5[] = "99e2.5 ";
    ASSERT_EQ(isNumber(s1), true);
    ASSERT_EQ(isNumber(s2), false);
    ASSERT_EQ(isNumber(s3), true);
    ASSERT_EQ(isNumber(s4), false);
    ASSERT_EQ(isNumber(s5), false);
}

//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}