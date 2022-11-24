print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#convert names to lower
name1_as_lower = name1.lower()
name2_as_lower = name2.lower()
# concatenate name as full name
full_names = name1_as_lower + name2_as_lower
# count for TRUE
count_true = 0
count_true += full_names.count("t")
count_true += full_names.count("r")
count_true += full_names.count("u")
count_true += full_names.count("e")
# count for love
count_love = full_names.count("l")
count_love += full_names.count("o")
count_love += full_names.count("v")
count_love += full_names.count("e")
#convert love score to string
love_score = str(count_true) + str(count_love)
love_score_as_int = int(love_score)

if (love_score_as_int < 10) or (love_score_as_int > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score_as_int) >= 40 and (love_score_as_int <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
