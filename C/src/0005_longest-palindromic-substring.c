//
/* Created by rock on 5/2/20.
*/
#include "leetcode_functions.h"
#include "mystr.h"

int expandAroundCenter(char *s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R <= strlen(s) - 1 && s[L] == s[R]) {
        L--;
        R++;
    }
    return R - L - 1;


}

//void substring(char *dest, char *src, int start, int end) {
//    int i = start;
//    if (start > strlen(src))return;
//    if (end > strlen(src))
//        end = strlen(src);
//    while (i < end) {
//        dest[i - start] = src[i];
//        i++;
//    }
//    dest[i - start] = '\0';
//    return;
//}
//
char *longestPalindrome(char *s) {
    if (strlen(s) < 1) {
        return "";
    }
//    printf("len:%d \n", strlen(s));
    int start = 0, end = 0;
    for (int i = 0; i < strlen(s); ++i) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    //    // 当时使用GTest测试 会 报错 Invalid Pointer...
//    //上面堆内存申请OK;原因是忘记了free
    printf("Start--End:%d--%d\n", start, end);
//    int ret_len = end - start + 1;
//    char * res;
//    res = (char *) malloc(ret_len+1);
//    substring(res, s, start, end+1);
//
//    return res;

    int ret_len = end - start + 1;
    s[end + 1] = '\0';
    return s + start;

}





//
//char * longestPalindrome(char * s){

//    if(strlen(s)==0||strlen(s)==1) return s;
//    int i,start,left,right,count,len;
//    start = len =0;
//    for(i=0;s[i]!='\0';i+=count){
//        count = 1;
//        left=i-1;
//        right = i+1;
//        while(s[right]!='\0'&&s[i]==s[right]){ //处理重复字符串
//            right++;
//            count++;
//        }
//        while(left>=0 && s[right]!='\0' && s[left] == s[right]){
//            left--;
//            right++;
//        }
//        if(right-left-1>len){
//            start = left+1;
//            len = right-left-1;
//        }
//    }
//    s[start + len] = '\0';      // 原地修改返回
//    return s + start;
//}
//
