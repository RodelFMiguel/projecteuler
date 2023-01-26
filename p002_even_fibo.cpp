#include <iostream>

#define FIBO_MAX 4000000

int even_fibo = 0;

int fibo(int max)
{
    int first = 0, second = 1, sum = 0, iterations = 0;

    do {
        sum = first + second;
        first = second;
        second = sum;

        if (sum % 2 == 0)
            even_fibo += sum;

        iterations++;

    } while (sum < max);

    std::cout << "iterations: " << iterations << std::endl;
    return sum;
}

int main()
{
    std::cout << "fibo sum: " << fibo(FIBO_MAX) << std::endl;
    std::cout << "even fibo sum: " << even_fibo << std::endl;
}