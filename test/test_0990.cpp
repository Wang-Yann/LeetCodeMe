//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(equationsPossible, test1) {
    char *equations[] = {"a==b", "b!=a"};
//    printf("Size:%d", sizeof(equations) / sizeof(char *));
    bool result = equationsPossible(equations, sizeof(equations) / sizeof(char *));
    ASSERT_FALSE(result);
    char *equations1[] = {"b==a", "a==b"};
    bool result1 = equationsPossible(equations1, sizeof(equations1) / sizeof(char *));
    ASSERT_TRUE(result1);
    char *equations2[] = {"a==b", "b==c", "a==c"};
    bool result2 = equationsPossible(equations2, sizeof(equations2) / sizeof(char *));
    ASSERT_TRUE(result2);
    char *equations3[] = {"a==b", "b!=c", "c==a"};
    bool result3 = equationsPossible(equations3, sizeof(equations3) / sizeof(char *));
    ASSERT_FALSE(result3);
    char *equations4[] = {"c==c", "b==d", "x!=z"};
    bool result4 = equationsPossible(equations4, sizeof(equations4) / sizeof(char *));
    ASSERT_TRUE(result4);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
