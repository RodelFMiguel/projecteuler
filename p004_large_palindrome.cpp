#include <iostream>
#include <string>

bool is_palindrome(int pal)
{
    std::string str = std::to_string(pal);
    for (int i = 0, j = str.length() - 1; i < (str.length()/2); i++, j--) {
        if (str.c_str()[i] != str.c_str()[j]) return false;
    }
    return true;
}

int main()
{
    int x_max = 0, y_max = 0, pal_max = 0;

    for (int x = 999; x >= 100; x--) {
        for (int y = x; y >= 100; y--) {
            if (is_palindrome(x*y)) {
                if (pal_max < x*y) {
                    pal_max = x*y;
                    break;
                }
            }
        }
    }

    std::cout << "Largest 3 Digit Palindrome: " << pal_max << std::endl;
    std::cout << "x, y: (" << x_max << ", " << y_max << ")" << std::endl;
}