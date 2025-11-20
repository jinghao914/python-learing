#include <stdio.h>

int MaxSubseqSum1(int A[], int N)
{
    int ThisSum, Maxsum = 0;
    int i, j, k;
    for (i = 0; i < N; i++)
    {
        for (j = i; j < N; j++)
        {
            ThisSum = 0;
            for (k = i; k <= j; k++)
            {
                ThisSum += A[k];
            }
            if (ThisSum > Maxsum)
                Maxsum = ThisSum;
        }
    }
    return Maxsum;
}

// 必须要有main函数
int main()
{
    int arr[] = {1, -2, 3, 5, -1, 2};
    int n = 6;
    int result = MaxSubseqSum1(arr, n);
    printf("最大子序列和为: %d\n", result);
    return 0;
}
