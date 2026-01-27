#include <iostream>
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
    //Limits random number to true or false
    std::bernoulli_distribution dist(.5); 
    
    //Tracks the beginning of running, to track time taken
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < totalFlips; i++) {
        if (dist(gen)) {
            heads++;//Adds 1 to heads if we roll a true
        }
        if (i % (totalFlips/20) == 0) { //If int i is 5% of total flips (5%, 10%, 15%)
            std::cout << "Completed: " << (i*100/totalFlips) << "% " << i << '/' << totalFlips << std::endl;
        }
    }
    //Tracks the end of running, to track time taken
    auto end = std::chrono::high_resolution_clock::now();
    //Finds difference in start and end times
    std::chrono::duration<double> duration = end - start;

    tails = totalFlips - heads;//Get tails (more efficient than settings both in the for loop)

    std::cout << "\nResults:" << std::endl;
    std::cout << "Heads: " << heads << std::endl;
    std::cout << "Tails: " << tails << std::endl;
    std::cout << "Time taken: " << duration.count() << " seconds" << std::endl; //Time taken
}