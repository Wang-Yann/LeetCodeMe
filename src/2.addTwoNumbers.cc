#include "headers.h"

class Solution
{
public:
    int addTwoNumbers(vector<int> &nums)
    {
        return 1;
    }
};

TEST(addTwoNumbers, addTwoNumbers_1)
{
    Solution s;
    vector<int> in = {1, 2, 3};
    int ans = 12;
    EXPECT_EQ(s.addTwoNumbers(in), ans);
}

int main(int argc, char **argv)
{
    printf("%s","hello world\n");
    ::testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}