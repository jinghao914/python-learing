#include <stdio.h>
int main()
{
    int x = 2; // 从2开始检查
    int cnt = 0;

    while (cnt < 50)
    {
        int isPrime = 1; // 假设x是素数

        // 判断x是否为素数
        for (int i = 2; i < x; i++)
        {
            if (x % i == 0)
            {
                isPrime = 0; // 能被整除，不是素数
                break;
            }
        }

        // 如果是素数，输出并计数
        if (isPrime == 1)
        {
            printf("%d ", x); // 修正：使用x而不是&x，添加分号
            cnt++;            // 添加分号
        }

        x++; // 检查下一个数字
    }

    return 0;
}