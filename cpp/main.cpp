#include <fstream>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <curl/curl.h>


#include "main.h"
#include "checks.h"
#include "funcs.h"
#include "mathfuncs.h"
#include "stack.h"
#include "tokenList.h"

#include "paramstrings.h"

const char* liburl = "https://raw.githubusercontent.com/MeanTheBean/mtb-lang/refs/heads/master/libs/";


void write_file(const char* path, unsigned char* data, unsigned int len) 
{
    std::ofstream out(path, std::ios::binary);
    out.write((char*)data, len);
}

size_t write_callback(void* ptr, size_t size, size_t nmemb, void* userdata)
{
    FILE* file = (FILE*)userdata;
    return fwrite(ptr, size, nmemb, file);
}

bool download_package(const std::string& pkg_name)
{
    CURL* curl = curl_easy_init();
    if (!curl)
        return false;

    std::string url  = std::string(liburl) + pkg_name + ".mtb";
    std::string path = "/tmp/mtb/" + pkg_name + ".mtb";

    FILE* file = fopen(path.c_str(), "wb");
    if (!file)
    {
        curl_easy_cleanup(curl);
        return false;
    }

    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);

    CURLcode res = curl_easy_perform(curl);

    fclose(file);
    curl_easy_cleanup(curl);

    if (res != CURLE_OK)
    {
        std::cerr << "Failed to download " << pkg_name
                  << ": " << curl_easy_strerror(res) << '\n';
        return false;
    }

    return true;
}

void install_package(char** packages, int pcount)
{
	system("mkdir -p /tmp/mtb");

	std::vector<std::string> pkgs(pcount-2);
	for (int i = 2; i < pcount; i++)
	{
		std::string pkg = packages[i];
		std::cout << "Installing " << pkg << "...\n";

		if (!download_package(pkg))
			std::cerr << "Failed!\n";
		else
			std::cout << "Done!\n";
	}
	
	std::cout << '\n';
}

int main(int argc, char** argv)
{
	curl_global_init(CURL_GLOBAL_DEFAULT);

	if (argc < 2)
		std::cout << "ERROR: No input file specified\n\trun \"mtb --help\" for more info\n";
	else if (std::string(argv[1]) == "--help")
		std::cout << helptext << '\n';
	else if (std::string(argv[1]) == "install")
		install_package(argv, argc);
	else
	{
		system("mkdir -p /tmp/mtb");

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

	curl_global_cleanup();
}
