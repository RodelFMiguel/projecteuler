#include <iostream>
#include <cmath>

bool is_prime(long number)
{
    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(int i = 3; i <= sqrt(number); i+=2){
        if(number % i == 0 ) return false;
    }
    return true;
}

long sum_of_primes(int max)
{
    long sum_primes = 0;
    std::cout << "(primes: ";
    for (int i = 2; i < max; i++) {
        if (is_prime(i)) {
            sum_primes += i;
            std::cout << i << " ";
        }
    }
    std::cout << ") ";
    return sum_primes;
}

int main()
{
    std::cout << "sum of primes below 10: " << sum_of_primes(10) << std::endl;
    std::cout << "sum of primes below 2000000: " << sum_of_primes(2000000) << std::endl;
}