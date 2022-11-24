# Day 004 - Randomisation and Python lists

# Treasure Map
You are going to write a program that will mark a spot with an  `X`.

In the starting code, you will find a variable called  `map`.

This  `map`  contains a nested list. When  `map`  is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code  `print(f"{row1}\n{row2}\n{row3}"`  to format the 3 lists to be printed as a 3 by 3 square, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']
oYour job is to write a program that allows you to mark a square on the map using a two-digit system.

The  **first digit**  in the input will specify the  **column**  (the position on the horizontal axis).

The  **second digit**  in the input will specify the  **row**  number (the position on the vertical axis).

So an input of 23 should place an X at the position shown below:

First, your program must take the user input and convert it to a usable format.

Next, you need to use that input to update your nested list with an "x". Remember that your nested list  `map`  actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

## Example Input 1

column 2, row 3 would be entered as:

```plaintext
23

```

## Example Output 1

```plaintext
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```

# Rock Pape Scissors
# Instructions

Make a rock, paper, scissors game. 

Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console. 

Start the game by asking the player:

*"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

From there you will need to figure out: 
* How you will store the user's input.
* How you will generate a random choice for the computer.
* How you will compare the user's and the computer's choice to determine the winner (or a draw).
* And also how you will give feedback to the player. 

You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)
