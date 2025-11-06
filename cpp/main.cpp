#include <fstream>
#include <cstdlib>
#include <iostream>
#include <string>

#include "main.h"
#include "checks.h"
#include "funcs.h"
#include "mathfuncs.h"
#include "stack.h"
#include "tokenList.h"


void write_file(const char* path, unsigned char* data, unsigned int len) 
{
    std::ofstream out(path, std::ios::binary);
    out.write((char*)data, len);
}

int main(int argc, char** argv)
{
	if (argc < 2)
		std::cout << "ERROR: No input file specified\n\trun \"mtb --help\" for more info\n";
	else
	{
		system("mkdir -pv /tmp/mtb");

		write_file("/tmp/mtb/main.py", main_py, main_py_len);
		write_file("/tmp/mtb/checks.py", checks_py, checks_py_len);
		write_file("/tmp/mtb/funcs.py", funcs_py, funcs_py_len);
		write_file("/tmp/mtb/mathfuncs.py", mathfuncs_py, mathfuncs_py_len);
		write_file("/tmp/mtb/stack.py", stack_py, stack_py_len);
		write_file("/tmp/mtb/tokenList.py", tokenList_py, tokenList_py_len);
		
		std::string ar =  "python3 /tmp/mtb/main.py ";
		ar += argv[1];
		system(ar.c_str());
	}
}
