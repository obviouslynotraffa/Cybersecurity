# Write4

### 📄 Description

### Cord cut
Our favourite string `/bin/cat flag.txt` is not present this time. Although you'll see later that there are other ways around this problem, such as resolving dynamically loaded libraries and using the strings present in those, we'll stick to the challenge goal which is learning how to get data into the target process's virtual address space via the magic of ROP.

### Differences
Things have been rearranged a little for this challenge; the printing logic has been moved into a separate library. The stack smash also takes place in a function within that library, but don't worry, this will have no effect on your ROP chain. A PLT entry for a function named `print_file()` exists within the challenge binary, simply call it with the name of a file you wish to read (like "flag.txt") as the 1st argument.

### Read/Write
The important thing to realise is that ROP is just a form of arbitrary code execution and if we're creative we can leverage it to do things like write to or read from memory. The question is what mechanism are we going to use to solve this problem, is there any built-in functionality to do the writing or do we need to use gadgets? In this challenge we won't be using built-in functionality since that's too similar to the previous challenges, instead we'll be looking for gadgets that let us write a value to memory such as `mov [reg], reg`.

### What/Where
Perhaps the most important thing to consider in this challenge is where we're going to write our "flag.txt" string. Use rabin2 or readelf to check out the different sections of this binary and their permissions. Learn a little about ELF sections and their purpose. Consider how much space each section might give you to work with and whether corrupting the information stored at these locations will cause you problems later if you need some kind of stability from this binary.

### Decisions, decisions
Once you've figured out how to write your string into memory and where to write it, go ahead and call `print_file()` with its location as your only argument. 

### ⚙ How to run it
```bash
./write4
```

### ⛔ Rules
Don't open the `flag.txt` file.
