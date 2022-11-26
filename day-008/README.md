# Day-008

## Exercise 1 - Paint Area Calculator
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

## Exercise 2- Prime Numbers
### Instructions

Prime numbers are numbers that can only be cleanly divided by themselves and 1.

[https://en.wikipedia.org/wiki/Prime_number](https://en.wikipedia.org/wiki/Prime_number)

**You need to write a function**  that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

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
