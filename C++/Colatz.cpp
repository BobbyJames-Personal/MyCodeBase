#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <string>
#include <limits>

unsigned long long userMax;
unsigned long long subStep = 1;
unsigned long long maxStartingNum = 1;
unsigned long long maxSubStepFound = 1;

std::vector<unsigned long long> cache = {};
std::unordered_set<unsigned long long> previousNumbers = {0, 1};

// Collatz conjecture:
// Even: n/2
// Odd: 3n+1
int main() {
    // If statement source: (std::find) 
    // Source - https://stackoverflow.com/a/571405
    // Posted by MSN, modified by community. See post 'Timeline' for change history
    // Retrieved 2026-06-06, License - CC BY-SA 4.0
    std::cout << "This will set the maximum number checked (inclusive) \n";
    std::cout << "Please input a positive integer: ";
    std::cin >> userMax;

    
    // If the sub-step number is not one of the previous numbers
    for (unsigned long long n = 1; n <= userMax; n++) {
        subStep = n;
        cache.clear();
        cache.push_back(subStep);
        while (previousNumbers.find(subStep) == previousNumbers.end()) {
            if (subStep % 2 == 0) {
                subStep = subStep / 2;
            } else {
                subStep = 3 * subStep + 1; 
            }
            cache.push_back(subStep);
            if (subStep > maxSubStepFound) {
                maxSubStepFound = subStep;
                maxStartingNum = n;
            }
        }

        // Appends cache to the previousNumbers list
        previousNumbers.insert(cache.begin(), cache.end()); 
    }
    
    std::vector<unsigned long long > sortedVector(previousNumbers.begin(), previousNumbers.end());
    std::sort(sortedVector.begin(), sortedVector.end());
    
    std::cout << "Checked all numbers!\n";
    std::cout << "Starting number that gave the largest number: " << maxStartingNum << "\n";
    std::cout << "Largest number: " << sortedVector.back() << std::endl;

    std::string print = "N";
    std::cout << "Would you like to print all found numbers? (" << sortedVector.size() << " elements) y/N ";
    std::cin >> print;

    if (print == "y" || print == "Y") {
        for (unsigned long long element : sortedVector) {
            std::cout << element << "\n";
        }
    }
    std::_Exit(0); 
}