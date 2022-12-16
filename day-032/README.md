# Day 32 - Send Email (smtplib) & Manage Dates (datetime)
## motivational-quotes
- Send email of a motivational quote every monday
- Use  datetime module to obtain the current day of the week
- Open the quotes.txt file and obtain a list of quotes
- Use the random module to pick a random quote of your list of quotes
- Use the smtplib to send the email to yourself

## birthday-wisher project
Checks date in birthday.csv if today is someone's birthday select random letter and mail it to the person
1. Update the birthdays.csv with your friends & family's details.   

> name,email,year,month,day  
> YourName,your_own@email.com,today_year,today_month,today_day

2. Check if today matches a birthday in the birthdays.csv  
- HINT 1: Create a tuple from today's month and day using datetime. e.g.  
    
> today = (today_month, today_day)

- HINT 2: Use pandas to read the birthdays.csv 
- HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
  ```  
    birthdays_dict = {
        (birthday_month, birthday_day): data_row  
    }  
  ```
>  e.g. if the birthdays.csv looked like this:    
> name,email,year,month,day     Angela,angela@email.com,1995,12,24    
> Then the birthdays_dict should look like this:

  ```  
  birthdays_dict = {  
     (12, 24): Angela,angela@email.com,1995,12,24  
  }  
  ```
  
- HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys

3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv  
  
4. Send the letter generated in step 3 to that person's email address.  
- HINT: The message should have the Subject: Happy Birthday then after \n\n The Message Body.


> Written with [StackEdit](https://stackedit.io/).