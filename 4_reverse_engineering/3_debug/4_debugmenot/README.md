# Description
The program runs several checks to detect a debugging environment. If running into gdb, every test should FAIL. 
Patch the program to obtain PASS in every check even when running into gbd

## Solution
An easy way to solve this challenge is to make all the test function return 0.