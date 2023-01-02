# Day 03 - Control Flow and Logical Operators
## Goals and Tools
- Control Flow with if _ else and Conditional Operators 
- Nested if statements and elif statements 
- Multiple If Statements in Succession 
- Logical Operators

## [BMI 2.0](bmi-calculator-2.py)
- Program interprets the Body Mass Index (BMI) based on a user's weight and height.
- Advance program of [BMI calculator](../day-002/bmi-calculator.py)
- It should tell them the interpretation of their BMI based on the BMI value i.e.
    -  **underweight, normal weight, overweight, obese, clinically obese**.

### Example Input
```plaintext
weight = 85
height = 1.75
```

### Example Output

```plaintext
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight
```

## [Leap Year](leap-year.py)
- Program works out whether a given year is a leap year. 
- A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

[https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year.

> on every year that is evenly divisible by 4
> 
> **except** every year that is evenly divisible by 100
> 
> **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

### Example Input 1

```plaintext
2400
```

### Example Output 1

```plaintext
Leap year.
```

### Example Input 2

```plaintext
1989
```

### Example Output 2

```plaintext
Not leap year.
```

## [Pizza Order Program](pizza-order.py)

- Based on a user's order, work out their final bill.

### Example Input

```plaintext
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
```

### Example Output

```plaintext
Your final bill is: $28.
```


## [Love Calculator](love-calculator.py)
- Program that tests the compatibility between two people.

To work out the love score between two people:

> Take both people's names and check for the number of times the letters in the word TRUE occurs.
> 
> Then check for the number of times the letters in the word LOVE occurs.
> 
> Then combine these numbers to make a 2 digit number.

For Love Scores  **less than 10**  _or_  **greater than 90**, the message should be:

```plaintext
"Your score is **x**, you go together like coke and mentos."
```

For Love Scores  **between 40**  and  **50**, the message should be:

```plaintext
"Your score is **y**, you are alright together."
```

Otherwise, the message will just be their score. e.g.:

```plaintext
"Your score is **z**."
```

e.g.

```plaintext
name1 = "Angela Yu"
name2 = "Jack Bauer"
```

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

### Example Input 1

```plaintext
name1 = "Kanye West"
name2 = "Kim Kardashian"
```

### Example Output 1

```plaintext
Your score is 42, you are alright together.
```

### Example Input 2

```plaintext
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
```

### Example Output 2

```plaintext
Your score is 73.
```

## Project: [Treasure Island](treasure-island.py)
"Choose Your Own Adventure" game example. 