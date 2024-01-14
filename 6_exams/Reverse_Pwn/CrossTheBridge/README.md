# CrossTheBridge

### 📍 Description
Can you cross the bridge and get the flag?

### 📄 Rules
- You must not patch the `play_game_no_patch()` function, nor delete it, and this function must be executed to get the flag.
- The rest of the binary can be patched in any way you like!

## 🔑 Solution

There's a function that checks if the user has cheated using a `ptrace()` check, it's easily patched by changing a conditional jump to an unconditional one (`JZ`=>`JMP`)
The other patch consists in making the `generate_random_step()` function always return the same value by `NOP` the `seed` sets, so that the bridge isn't random anymore.

### 🚩 Flag

```plain
SPRITZ{WhaT_A_fUn_gAme}
```
