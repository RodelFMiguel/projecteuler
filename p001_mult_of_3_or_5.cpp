#include <iostream>


int main()
{
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if (!(i % 3) || !(i % 5))
            sum += i;
    }
    std::cout << "sum is: " << sum << std::endl;
}