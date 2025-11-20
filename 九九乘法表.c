#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int i = 1, j = 1;

    while (i <= n)
    {
        while (j <= i)
        {
            printf("%d*%d=%d", i, j, i * j);
            printf("\n");
            j++;
        }
        i++;
    }
    return 0;
}