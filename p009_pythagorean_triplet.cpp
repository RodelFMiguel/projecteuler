#include <iostream>

bool is_pythagorean_triplet(int a, int b, int c)
{
    if (a > b || b > c)
        return false;

    if ((a*a + b*b) == c*c)
        return true;
    else
        return false;
}

int main()
{
    for (int a = 1; a < 1000; a++) {
        for (int b = a+1; b < 1000; b++) {
            // for (int c = b+1; c < 1000; c++) {
                int c = 1000 - b - a;
                if ((a+b+c) == 1000) {
                    if (is_pythagorean_triplet(a, b, c)) {
                        std::cout << "pythagorean triplets: " << a << ", " << b << ", " << c << std::endl;
                        std::cout << "product: " << a * b * c << std::endl;
                    }
                }
            // }
        }
    }
}
