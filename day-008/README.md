# Day-008 - Function Parameters & Caesar Cipher
## Goals
- Functions with Inputs
- Positional vs. Keyword Arguments

## [Paint Area Calculator](paint-area-calc.py)
### Instructions

You are painting a wall. The instructions on the paint can says that  **1 can of paint can cover 5 square meters**  of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
number of cans = (wall height  **x**  wall width)  **÷**  coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 * 4) / 5
= 1.6

But because you can't buy 0.6 of a can of paint, the  **result should be rounded up**  to  **2**  cans.
IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
### Example Input
```plaintext
test_h = 3
test_w = 9
```
### Example Output
```plaintext
You'll need 6 cans of paint.
```

## [Prime Numbers](prime-numbers.py)
checks whether if the number passed into it is a prime number or not.

### Example Input 1
```plaintext
73
```

### Example Output 1
```plaintext
It's a prime number.
```

### Example Input 2
```plaintext
75
```

### Example Output 2
```plaintext
It's not a prime number.
```
## Project:  [Caesar-Cipher](caesar-cypher)
a program which encodes and decodes text