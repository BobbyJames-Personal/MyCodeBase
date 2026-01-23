#include <iostream>
#include <cstdlib>
#include <random>
#include <chrono>

long long totalFlips = 0;
//Heads and tails counts
long long heads = 0;
long long tails = 0;



    
int main() {
    //Gets the user's input, how many flips
    std::cout << "How many flips? ";
    std::cin >> totalFlips;

    //Uses <random> to generate a random seed
    std::random_device rd; 
    std::mt19937 gen(rd());
    //Limits random number to 1 or 2
    std::bernoulli_distribution dist(.5); 
    
    //Tracks the beginning of running, to track time taken
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < totalFlips; i++) {
        if (dist(gen)) {
            heads++;
        }
        if (i % (totalFlips/20) == 0) {
            long long test = i;
            std::cout << "Completed: " << (test*100/totalFlips) << "% " << test << '/' << totalFlips << std::endl;
        }
    }
    //Tracks the end of running, to track time taken
    auto end = std::chrono::high_resolution_clock::now();
    //Finds difference in start and end times
    std::chrono::duration<double> duration = end - start;

    tails = totalFlips - heads;

    std::cout << "\nResults:" << std::endl;
    std::cout << "Heads: " << heads << std::endl;
    std::cout << "Tails: " << tails << std::endl;
    std::cout << "Time taken: " << duration.count() << " seconds" << std::endl; //Time taken
}