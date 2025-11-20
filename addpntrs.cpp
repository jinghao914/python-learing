#include <iostream>

int main()
{
    using namespace std;
    double wages[3] = {1000.0, 2000.0, 3000.0};
    short stacks[3] = {3, 2, 1};
    double *pw = wages;
    cout << "pw= " << pw << ",*pw= " << *pw << endl;
    pw += 1;
    cout << "pw= " << pw << ",*pw= " << *pw << endl;
    cout << &wages << " " << *wages << endl;
    cout << "------------------" << endl;

    short *ps = &stacks[0];
    cout << "ps= " << ps << ",*ps " << *ps << endl;
    ps += 1;
    cout << "ps= " << ps << ",*ps= " << *ps << endl;

    cout << "stacks[0] = " << stacks[0] << " " << "stacks[1]= " << stacks[1] << endl; // 数组名可以像指针一样
    cout << "stacks = " << stacks << " " << "&stacks[0]= " << stacks[0] << endl;      // 数组名是首地址，&接地址（数组名）取指向该地址的值
    cout << "*(stacks + 1)= " << *(stacks + 1) << endl;
    /*
    数组名可以当作指针来使用，它大多数情况下可以当作地址，但使用sizeof()时不行
    */

    return 0;
}