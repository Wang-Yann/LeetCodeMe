#include "leetcode_functions.h"



//leetcode submit region begin(Prohibit modification and deletion)

int climbStairs(int n){
    int prev=0;
    int cur=1;
    for(int i=0;i<n;i++){
        int temp = prev;
        prev=cur;
        cur=cur+temp;
    }
    return cur;
}


//leetcode submit region end(Prohibit modification and deletion)



