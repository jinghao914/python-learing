#include <stdio.h>

int main() {
    double x, original_x, f;
    scanf("%lf", &x);
    original_x = x;  // 保存原始值
    
    int sign;
    if (x > 0) {
        sign = 1;
    } else if (x < 0) {
        sign = -1;
    } else {
        sign = 0;
    }
    
    switch(sign) {
        case 1:
            f = 2 * original_x;  // 使用原始x值计算
            break;
        case -1:
            f = -1;
            break;
        case 0:
            f = 0;
            break;
    }
    
    printf("f = %.2f\n", f);
    return 0;
}