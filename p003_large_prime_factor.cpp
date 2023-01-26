#include <iostream>

void get_largest_prime_factor(long num)
{
    long x = num;
    while (x % 2 == 0) {
        x = x / 2;
        std::cout << "2\t";
    }

    for (long i = 3; (i^2) <= x; i += 2) {
        while (x % i == 0) {
            x = x / i;
            std::cout << i << "\t";
        }
    }

    if (x > 2)
        std::cout << x << "\t";

    std::cout << std::endl;
}

int main()
{
    long max = 600851475143;
    // long max =    900000000033;
    std::cout << "Prime factors of " << max << " is: ";
    get_largest_prime_factor(max);
}