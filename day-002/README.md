# Day 002 - Understanding Data Types and How to Manipulate Strings

## Goals and Tools
- Python Primitive Data Types 
- Type Error, Type Checking and Type Conversion 
- Mathematical Operations in Python 
- BMI Calculator 
- Number Manipulation and F Strings in Python 
- Life in Weeks 
- Project: Tip Calculator

## [BMI Calculator](bmi-calculator.py)
- Program calculates the Body Mass Index (BMI) from a user's weight and height.
- The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight. 
- The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/be5ff193-a1ad-4f8e-ba40-504c85610518/BMI+Image+Small.jpeg)

**Warning**  you should convert the result to a whole number.

### Example Input

```plaintext
weight = 80
height = 1.75
```

### Example Output

```plaintext
80 ÷ (1.75 x 1.75) = 26.122448979591837
26
```

## [Life in Weeks](life-in-weeks.py)

- Program uses maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
- It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

### Example Output

```plaintext
You have 12410 days, 1768 weeks, and 408 months left.
```

## [Project - Tip Calculator](tip-calculator.py)

## Instructions
- If the bill was $150.00, split between 5 people, with 12% tip. 
- Each person should pay (150.00 / 5) * 1.12 = 33.6 
- Format the result to 2 decimal places = 33.60
- Thus, everyone's share of the total bill is $30.00 plus a $3.60 tip.

## Example Input

```
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
```

## Example Output

```
Each person should pay: $19.93
```