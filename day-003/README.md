# Day 03

## Exercise 2 - BMI 2.0
### Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

-   Under 18.5 they are underweight
-   Over 18.5 but below 25 they have a normal weight
-   Over 25 but below 30 they are slightly overweight
-   Over 30 but below 35 they are obese
-   Above 35 they are clinically obese.

![](https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36)

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

![](https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/6653a739-6bc2-4d53-b566-67f5c0b32849/BMI+Image+Small.jpeg)

**Warning**  you should  **round**  the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g.  **underweight, normal weight, overweight, obese, clinically obese**.

### Example Input

```plaintext
weight = 85
height = 1.75
```

### Example Output

```plaintext
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly ove
```

## Exercise 3 - Leap Year
### Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

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

**Warning**  your output should match the Example Output format exactly, even the positions of the commas and full stops.

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

## Exercise 4 - Pizza Order Practice
### Instructions

Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15

Medium Pizza: $20

Large Pizza: $25

Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1

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


## Exercise 5 - Love Calculator

### Instructions

You are going to write a program that tests the compatibility between two people.

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

## Project: Treasure Island

### Instructions
Make your own "Choose Your Own Adventure" game. Use conditionals such as `if`, `else`, and `elif` statements to lay out the logic and the story's path in your program. 

### Text Snippets from my example

* 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"'
* 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
* "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
* "It\'s a room full of fire. Game Over."
* "You found the treasure! You Win!"
* "You enter a room of beasts. Game Over."
* "You chose a door that doesn\'t exist. Game Over."
* "You get attacked by an angry trout. Game Over."
* "You fell into a hole. Game Over."

[You can also add your own ASCII art](https://ascii.co.uk/art). Just remember to add three single quotes `'''` at the start and at the end of your artwork to turn it into a multi-line string. 

