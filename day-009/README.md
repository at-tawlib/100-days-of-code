# Day 009 - Dictionaries, Nesting and the Secret Auction
## Goals
- The Python Dictionary_ Deep Dive 
- Nesting Lists and Dictionaries 
- Dictionary in List 

## [Grading Program](grading-program.py)
### Instructions
You have access to a database of  `student_scores`  in the format of a dictionary. The  **keys**  in  `student_scores`  are the  **names**  of the students and the  **values**  are their exam  **scores**.

Write a program that  **converts their scores to grades**. By the end of your program, you should have a new dictionary called  `student_grades`  that should contain student  **names**  for  **keys**  and their  **grades**  for  **values**. T**he final version**  of the  `student_grades`  dictionary will be checked.

This is the scoring criteria:

> Scores 91 - 100: Grade = "Outstanding"
> 
> Scores 81 - 90: Grade = "Exceeds Expectations"
> 
> Scores 71 - 80: Grade = "Acceptable"
> 
> Scores 70 or lower: Grade = "Fail"

### Expected Output
```plaintext
'{'Harry': 'Exceeds Expectations', 'Ron': 'Acceptable', 'Hermione': 'Outstanding', 'Draco': 'Acceptable', 'Neville': 'Fail'}'
```

## [Dictionary in list](dictionary-in-list.py)
- a program that adds to a  `travel_log`. 
- Travel_log is a  **List**  that contains 2  **Dictionaries**.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the  `travel_log`.

```plaintext
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
```

> You've visited Russia 2 times.
> 
> You've been to Moscow and Saint Petersburg.

**DO NOT**  modify the  `travel_log`  directly. You need to create a function that modifies it.

## Project : [Blind Auction](blind-auction)
- a program that will collect the names and bids of different people. 
- The program should ask for each bidder's name and their bid individually. 

```
Welcome to the secret auction program. 
What is your name?: Angela
```
```
What's your bid?: $123
```
```
Are there any other bidders? Type 'yes' or 'no'.
yes
```
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid. 

```
The winner is Elon with a bid of $55000000000
```