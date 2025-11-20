#include <stdio.h>
int main() {
    //printf("输入成绩：")
    int score;
    scanf("%d", &score);
    printf("成绩等级为：");
    score /= 10;
    switch (score) {
        case 10:
        case 9:
            printf("A\n");
            break;
        case 8:
            printf("B\n");
            break;
        case 7:
            printf("C\n");
            break;
        case 6:
            printf("D\n");
            break;
        default:
            printf("E\n");
    }
}