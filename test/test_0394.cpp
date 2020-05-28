//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(decodeString, test1) {
    char s1[] ="3[a2[c]]";
    char expected[] = "accaccacc";
    char *res = decodeString(s1);

    ASSERT_TRUE(strcmp(expected,res)==0);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
