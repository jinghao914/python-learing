#include <stdio.h>
int main()
{
    int x;
    int one, two, five;

    scanf("%d", &x);
    for (one = 1; one < x * 10; one++)
    {
        for (two = 1; two < x * 5; two++)
        {
            for (five = 1; five < x * 2; five++)
            {
                if (x * 10 == one * 10 + two * 5 + five * 2)
                {
                    printf("%d元可以由%d个一角，%d个两角，%d个五角凑成\n", x, one, two, five);
                    goto out;
                }
            }
        }
    }
out:
    return 0;
}