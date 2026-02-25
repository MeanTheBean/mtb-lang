#!/bin/bash

./cpp/convert.sh
g++ -lcurl -o mtb ./cpp/main.cpp
