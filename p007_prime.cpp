#include <iostream>
#include <cmath>

bool is_prime(long x)
{
    if (x % 2 == 0)
        return false;

    for (int i = 3; i <= static_cast<int>(sqrt(x)); i+=2) {
        if (x % i == 0) {
            return false;
        }
    }

    return true;
}

long nth_prime(long n)
{
    if (n == 1)
        return 2;

    long last_prime = 2;
    for (long j = 3, i = 2; i <= n; j+=2) {
        if (is_prime(j)) {
            last_prime = j;
            i++;
        }
    }

    return last_prime;
}

int main()
{
    // std::cout << "sqrt: " << static_cast<int>(sqrt(23)) << std::endl;
    std::cout << "is prime: " << is_prime(9) << std::endl;
    std::cout << "10001st prime: " << nth_prime(10001) << std::endl;
}