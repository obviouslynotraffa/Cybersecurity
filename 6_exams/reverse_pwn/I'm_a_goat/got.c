#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/types.h>

// sysctl -w kernel.randomize_va_space=0
// gcc -m32 -o goat got.c -fno-stack-protector -znoexecstack -no-pie

void win() {
    printf("Nice! Here is your flag: spritz{GOT_not_Goat!}");
}

int main(int argc, char **argv) {

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[256];
  
  unsigned int address;
  unsigned int value;

  puts("Welcome. In this challenge you need to become the GOaT.\nI'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?");

  scanf("%x", &address);

  sprintf(buf, "Okay, now what value would you like to write to 0x%x", address);
  puts(buf);
  
  scanf("%x", &value);

  sprintf(buf, "Okay, writing 0x%x to 0x%x", value, address);
  puts(buf);

  *(unsigned int *)address = value;

  puts("Okay, exiting now...\n");
  exit(1);
  
}