//
/* Created by rock on 5/2/20.
*/
#include "leetcode_functions.h"

#define STR_LEN 5000

char *decodeStringRecu(char *s, char **e) {
    char *ret = (char *) malloc(sizeof(char) * STR_LEN);
    char *buf, *end = NULL;
    int count = 0, idx = 0;
    while (*s != '\0') {
        if (isalpha(*s)) {
            ret[idx++] = *s;
        } else if (isdigit(*s)) {
            count = 10 * count + *s - '0';
        } else if (*s == '[') {
            buf = decodeStringRecu(s + 1, &end);
            while (count) {
                strcpy(ret + idx, buf);
                idx += strlen(buf);
                count--;

            }
            s = end;
        } else if (*s == ']') {
            *e = s;
            ret[idx] = '\0';
            return ret;
        }
        s++;

    }
    ret[idx] = '\0';
    return ret;


}

char *decodeString(char *s) {
    char *end = NULL;
    return decodeStringRecu(s, &end);
}