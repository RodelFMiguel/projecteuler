#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

long collatz_series(long n)
{
    long chain_ctr = 0;
    long num = n;

    do {
        if (num%2)
            num = (num*3) + 1;
        else
            num = num / 2;
        chain_ctr++;
    } while (num > 1);
    
    std::cout << "N: " << n << "; Depth: " << chain_ctr << std::endl;
    return chain_ctr; 
}

std::map<long, long> collatz_map;

long collatz(long n)
{
    std::map<long, long>::iterator it = collatz_map.find(n);
    if (it != collatz_map.end()) {
        return collatz_map[n];
    }

    if (n%2) {
        collatz_map[n] = 2 + collatz((3 * n + 1) / 2);
    } else {
        collatz_map[n] = 1 + collatz(n / 2);
    }

    return collatz_map[n];
}

int main()
{
    collatz_map.insert(std::pair<long, long>(1, 1));

    long longest_chain = 1;
    long answer = 0;
    for (long i = 2; i < 1000000; i++) {
        long chain = collatz(i);
        if (chain > longest_chain) {
            longest_chain = chain;
            answer = i;
        }
    }

    std::cout << "Longest chain: " << longest_chain << "; Number with longest chain: " << answer << std::endl;
}