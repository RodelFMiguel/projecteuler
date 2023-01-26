#include <iostream>
#include <cmath>

long sum_of_squares(long num)
{
    if (num <= 1)
        return 1;

    return pow(num, 2.0) + sum_of_squares(num-1); 
}

long square_of_sum(long num)
{
    long sum = 0;
    for (long i = 1; i <= num; i++) {
        sum += i;
    }

    return pow(sum, 2.0);
}

int main()
{
    std::cout << "square of sum: " << square_of_sum(100) << std::endl;
    std::cout << "sum of squares: " << sum_of_squares(100) << std::endl;
    std::cout << "diff: " << square_of_sum(100) - sum_of_squares(100) << std::endl;
}