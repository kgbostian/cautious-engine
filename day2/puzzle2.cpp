#include <cstdio>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

typedef std::vector<std::string>::iterator iter;
typedef std::vector<std::string>::const_iterator citer;
typedef std::vector<std::string> vstring;

void read_input_file(std::string file_name, vstring &input_vector);
int solve_puzzle(vstring &input_vector);


int main()
{
    vstring input;
    read_input_file("input", input);
    printf("\r\n%d\r\n", solve_puzzle(input));
    return 0;
}

int solve_puzzle(vstring &input_vector)
{
    int number_of_twos = 0;
    int number_of_threes = 0;
    for(iter it = input_vector.begin(); it != input_vector.end(); ++it)
    {
        std::string line = *it;
        bool firstPair = true;
        bool firstTriplet = true; 
        while(line.size() > 0)
        {
            char character = line.at(0);
            int count = std::count(line.begin(), line.end(), character);
            //printf("Countings %c's: %d\r\n", character, count);
            //printf("Size of line: %d\r\n", line.size());
            //printf("Contents of line: %s\r\n", line.c_str());
            for(int i = 0; i < count; i++)
            {    
                line.erase(line.find(character, 0), 1);
            }
            //printf("Size of line after removal: %d\r\n", line.size());
            if(count == 2 && firstPair)
            {
                number_of_twos++;
                firstPair = false;
                //printf("There are two.");
            }
            else if(count == 3 && firstTriplet)
            {
                number_of_threes++;
                firstTriplet = false;
                //printf("There are three.");
            }
            if(firstPair == false && firstTriplet == false)
                break;
        }
        //printf("End line processing.\r\n");
        printf("Number of 2s: %d\r\nNumber of 3s: %d\r\n", number_of_twos, number_of_threes);
    }   
    return number_of_twos * number_of_threes;
}

void read_input_file(std::string file_name, std::vector<std::string> &input_vector)
{
    std::ifstream input_file;
    std::string value = "";
    input_file.open(file_name);
    while(input_file >> value)
    {
        input_vector.push_back(value);
    }
    input_file.close();    
}
