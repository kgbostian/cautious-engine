#include <cstdio>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

void read_input_file(std::string file_name, std::vector<int> &input_vector);
int solve_puzzle(const std::vector<int> &input_vector);
int check_dup(int freq, std::vector<int> &dups);

int main()
{
    std::vector<int> input;
    read_input_file("input", input);
    printf("\r\n%d\r\n", solve_puzzle(input));
    return 0;
}

int solve_puzzle(const std::vector<int> &input_vector)
{
    int frequency = 0;
    std::vector<int> duplicates;
    duplicates.push_back(frequency);
    int size = input_vector.size();
    int i = 200;
    while(i-- > 0)
    {
        for(int i = 0; i < size; i++)
        {
            frequency += input_vector[i];
            if(check_dup(frequency, duplicates))
            {
                return frequency;
            }
        }
    }   
    return 0;
}

int check_dup(int freq, std::vector<int> &dups)
{
    std::vector<int>::iterator it = std::find(dups.begin(), dups.end(), freq);
    if( it == dups.end())
    {
        dups.push_back(freq);
        return false;
    }
    else
    {
        return true;
    }
}

void read_input_file(std::string file_name, std::vector<int> &input_vector)
{
    std::ifstream input_file;
    int value = 0;
    input_file.open(file_name);
    while(input_file >> value)
    {
        input_vector.push_back(value);
    }
    input_file.close();    
}
