#include <iostream>
#include <cmath>

long divisor_count(long num)
{
    long div = 0;
    for (int i = 1; i*i <= num; i++) {
        if (num % i == 0) {
            div += 2; // add 2 because you can divite num by i and num
            if (num / i == i) {
                div --;
            }
        }
    }

    return div;
}

long factor_count(long limit)
{
    for (int i = 1; i <= limit; i++) {
        int count = 1;
        if (i%2 == 0) {
            count = divisor_count(i/2) * divisor_count(i+1);
        } else {
            count = divisor_count(i) * divisor_count((i+1)/2);
        }
        std::cout << "factor count for " << i << " is " << count << std::endl;
        if (count > 500)
            return i;
    }
    return 1;
}

int main()
{
    long count = factor_count(500000);
    long triangle = (count) * (count + 1) / 2;
    std::cout << "count: " << count << std::endl;
    std::cout << "first triangle num with 500 divisors: " << triangle << std::endl;
}
