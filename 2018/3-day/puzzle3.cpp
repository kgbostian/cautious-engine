#include <cstdio>
#include <fstream>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

typedef std::vector<std::string>::iterator iter;
typedef std::vector<std::string>::const_iterator citer;
typedef std::vector<std::string> vstring;

struct data_input
{
    std::string id;
    int start_x;
    int start_y;
    int size_x;
    int size_y;
};


void read_input_file(std::string file_name, vstring &input_vector);
std::string solve_puzzle(vstring &input_vector);
void populate_grid(char [][1000]);
void split_data(std::string input);


int main()
{
    vstring input;
    char grid[1000][1000];
    populate_grid(grid);
    read_input_file("input", input);
    return 0;
}

void populate_grid(char grid[1000][1000])
{
    for(int i = 0; i < 1000; i++)
    {
        for(int j = 0; j < 1000; j++)
        {
            grid[i][j] = '.';
        }
    }
}
std::string solve_puzzle(vstring &input_vector)
{
    return "FAIL";
}

void split_data(std::string input)
{
    std::string delimiter = " ";
    size_t pos = 0;
    std::string token;

    data_input element;

    while ((pos = input.find(delimiter)) != std::string::npos) 
    {
        token = input.substr(0, pos);
        std::cout << token << std::endl;
        input.erase(0, pos + delimiter.length());
    }
}

void read_input_file(std::string file_name, std::vector<std::string> &input_vector)
{
    printf("Begin reading file\r\n");
    std::ifstream input_file;
    std::string value = "";
    input_file.open(file_name);
    while(input_file >> value)
    {
        printf("Line from file: %s\r\n", value.c_str());
        input_vector.push_back(value);
        split_data(value);
    }
    input_file.close();    
}
