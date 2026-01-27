#include <iostream>
#include <random>
#include <chrono>

int listLength;


int main() {
    std::cout << "How many elements? ";
    std::cin >> listLength; //User input for length of list
    float list[listLength]; //List of floats to sort
    
    //Before generation time
    auto preGen = std::chrono::high_resolution_clock::now();
    
    //Uses <random> to generate a random seed
    std::random_device rd; 
    std::mt19937 gen(rd());
    //Limits random number to true or false
    std::uniform_real_distribution<float> dist(0.0f, 10.0f);

    for (int i = 0; i < listLength; i++) { //Create random list of floats
        list[i] = dist(gen);
    }

    //Tracks the beginning of running, to track time taken
    auto postGen = std::chrono::high_resolution_clock::now();

    bool sorted = false;
    bool smallSorted = false;
    while (!sorted) {
        smallSorted = true;
        for (int i = 0; i + 1 < listLength; i++) {
            if (list[i] > list[i+1]) {
                float temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
                smallSorted = false;
            }
        }
        sorted = smallSorted;        
    }

    //Tracks the end of running, to track time taken
    auto end = std::chrono::high_resolution_clock::now();
    //Finds difference in start and end times
    std::chrono::duration<double> totalTime = end - preGen;
    std::chrono::duration<double> sortTime = end - postGen;

    std::cout << "List Sorted!" << std::endl;
    std::cout << "Total time taken: " << totalTime.count() << " seconds" << std::endl; //Time taken
    std::cout << "Sort time taken: " << sortTime.count() << " seconds" << std::endl; //Time taken
    
    char print = ' ';
    std::cout << "Print list? y/n ";
    std::cin >> print;

    if (print == 'Y' or print == 'y') {
        if (listLength < 500) {
            for (int i = 0; i < listLength; i++) {//Print list 
                std::cout << list[i] << std::endl;
            } 
        } else {
            for (int i = 0; i < listLength; i++) {//Print list 
                std::cout << list[i] << " | ";
            } 
            std::cout << " " << std::endl;
        }
    }
}