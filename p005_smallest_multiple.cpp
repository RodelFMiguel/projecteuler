#include <iostream>

bool is_divisible(long max, long multiple)
{
    for (long i = 2; i <= max; i++) {
        if (multiple % i) {
            return false;
        }
    }
    return true;
}

long smallest_multiple(long max)
{
    for (int i = max; ; i+=max) {
        if (is_divisible(max, i))
            return i;
    }
    return -1;
}

long gcd(long a, long b)
{
    return (b == 0) ? a : gcd (b, a%b);
}

int main()
{
    std::cout << "Min multiple 1..20: " << smallest_multiple(20) << std::endl;

    std::cout << "GCD: " << gcd(21, 48) << std::endl;
}