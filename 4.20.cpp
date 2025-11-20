#include <iostream>

int main()
{
    using namespace std;
    char animal[20] = "bear";
    const char *bird = "wren";
    /*
    变量名animal是一个char的地址，"wren"是被括起来的字符串，它也是一个地址
    但是用cout打印时，字符串和char不会被打印成地址
    其他类型，比如int就可以
    */
    int zhsh[20] = {1, 2, 3};
    cout << animal << "  " << bird << endl;
    cout << zhsh << endl;

    char brid1[20] = "wren";
    char *ps = brid1;
    cout << brid1 << " at " << (int *)ps << endl;
    cout << "-------------------" << endl;
    cout << &brid1;

    return 0;
}