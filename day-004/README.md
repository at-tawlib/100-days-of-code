# Day 004 - Randomisation and Python lists
## Goals and Tools
- Random Module
- Understanding the Offset and Appending Items to Lists
- IndexErrors and Working with Nested Lists

## [Treasure Map](treasure-map.py)
- Program that allows you to mark a square on the map using a two-digit system.
- The  **first digit**  in the input will specify the  **column**  (the position on the horizontal axis).
- The  **second digit**  in the input will specify the  **row**  number (the position on the vertical axis).
 `map`  contains a nested list. 
- When  `map`  is printed this is what the nested list looks like:

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']

    ['⬜️', '⬜️', '⬜️']

- So an input of 23 should place an X at the position shown below:
- First, your program must take the user input and convert it to a usable format. 
- Next, you need to use that input to update your nested list with an "x".

### Example Input 1
column 2, row 3 would be entered as:
```plaintext
23
```

### Example Output 1
```plaintext
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', 'X', '⬜️']
```

## [Rock Paper Scissors](rock-paper-scissors.py)
- Make a rock, paper, scissors game. 
- You can find the "official" rules of the game on [the World Rock Paper Scissors Association website.](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/)