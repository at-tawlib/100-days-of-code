# Day 026- List Compreshension and the NATO Alphabet
## Exercise 1 - Squaring numbers
**Instructions**
You are going to write a List Comprehension to create a new list called  `squared_numbers`. This new list should contain every number in the list  `numbers`  but each number should be squared.
e.g.
```plaintext
4 * 4 = 16
```

4 squared equals 16.

**DO NOT**  modify the List  `numbers`  directly. Try to use  **List Comprehension**  instead of a  **Loop**.

**Example Output**
```plaintext
[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
```

## Exercise 2 - Filtering Even Numbers
**Instructions**
You are going to write a List Comprehension to create a new list called  `result`. This new list should only contain the even numbers from the list  `numbers`.
**DO NOT**  modify the List  `numbers`  directly. Try to use  **List Comprehension**  instead of a  **Loop**.
**Example Output**
```plaintext
[2, 8, 34]
```

## Exercise 3 - Data Overlap
**Instructions**
Take a look inside  **file1.txt**  and  **file2.txt**. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are  **common**  in both files.
e.g. if file1.txt contained:

```plaintext
1
2
3
```

and file2.txt contained:

```plaintext
2
3
4
```
result = [2, 3]
**IMPORTANT**: The result should be a list that contains  **Integers**, not  **Strings**. Try to use  **List Comprehension**  instead of a  **Loop**.
**Example Output**
```plaintext
[3, 6, 5, 33, 12, 7, 42, 13]
```
## Exercise 4 - Dictionary Comprehension 1
**Instructions**
You are going to use Dictionary Comprehension to create a dictionary called  `result`  that takes each word in the given sentence and calculates the number of letters in each word.
**Do NOT**  Create a dictionary directly. Try to use  **Dictionary Comprehension**  instead of a  **Loop**.
**Example Output**

```plaintext
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
}
```
## Exercise 5 - Dictionary Comprehension 2
**Instructions**
You are going to use Dictionary Comprehension to create a dictionary called  `weather_f`  that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.
`To convert temp_c into temp_f:`
`(temp_c * 9/5) + 32 = temp_f`
**Do NOT**  Create a dictionary directly. Try to use  **Dictionary Comprehension**  instead of a  **Loop**.
**Example Output**
`{`

`'Monday': 53.6,`

`'Tuesday': 57.2,`

`'Wednesday': 59.0,`

`'Thursday': 57.2,`

`'Friday': 69.8,`

`'Saturday': 71.6,`

`'Sunday': 75.2`

`}`

## Project: NATO Phonetic Alphabet
- Use NATO alphabet to convert  a word.
- It takes each character of a word and matches it to the corresponding NATO Alphabet
 ```
 Enter a word: Thomas
 ['Tango', 'Hotel', 'Oscar', 'Mike', 'Alfa', 'Sierra']
 ```
- Catch the KeyError when a user enters a character that is not in the dictionary
- Provide the feedback to the user when an illegal word is entered.
- Continue prompting the user to enter another word until they entered a valid word.

 ***Steps***
 - Create a dictionary in this format:
 `{"A": "Alfa", "B": "Bravo"}`

 - Create a list of the phonetic code words from a word that the user inputs.


> Written with [StackEdit](https://stackedit.io/).
