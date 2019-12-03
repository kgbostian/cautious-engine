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

void read_input_file(std::string file_name, vstring &input_vector);
std::string solve_puzzle(vstring &input_vector);


int main()
{
    vstring input;
    read_input_file("input", input);
    std::cout << solve_puzzle(input) << std::endl;
    return 0;
}

std::string solve_puzzle(vstring &input_vector)
{
    vstring copy_vector = vstring(input_vector);
    std::vector<std::array<std::string, 2>> all_results;
    std::array<std::string,2> results;
    int index = 0;
    bool done = false;
    for(iter cit = input_vector.begin(); cit != input_vector.end(); ++cit)
    {
        vstring copy_vector = vstring(input_vector);
        copy_vector.erase(std::find(copy_vector.begin(), copy_vector.end(),(*cit)));
        for(iter it = copy_vector.begin(); it != copy_vector.end(); ++it)
        {
            int diff = 0;
            for(int i = 0; i < (*it).size(); i++)
            {
                if((*cit).at(i) != (*it).at(i))
                {
                    diff++;
                    index = i;
                }
                if(diff > 1)
                    break;
            }
            if(diff == 1)
            {
                results[0] = (*cit);
                results[1] = (*it);
                all_results.push_back(results);
                done = true;
                break;
            }
        } 
        if(done)
            break;
   }
   return results[1].erase(index,1);
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
