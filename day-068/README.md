# Day 068 - Authentication with Flask

## Goals
- What is Authentication
- Register New Users
- Downloading Files
- Login and Registering Users with Authentication
- Encryption and Hashing
- Hashing  and Salting Passwords using Werkzeug
- Authenticating Users with Flask-Login
- Flask Flash Messages
- Passing Authentication Status to Templates
- Register, login and logout users with email and password
- Allow registered users to download a top-secret [Flask Programming Cheat Sheet](static/files/cheat_sheet.pdf)

### [index.html](templates/index.html)
- First page which shows login and register buttons 
- Both login and register buttons are hidden
- Uses authentication to hide or show the buttons (i.e if user is authenticated, buttons are hidden)

### [register.html](templates/register.html)
- Registers new user 
- Get username, email and password and add it to the database
- If email already exists, show message to login rather and redirects to login page
- Once user is registered, goto secrets.html

### [login.html](templates/login.html)
- Shows a form for user to login
- compares email and password to data in the database
- if email or password is not correct, show error message
- if email and password is verified, redirect to [secrets page](templates/secrets.html)

### [secrets.html](templates/secrets.html)
- Displays "Hello <username>" after successfully creating a user or logging in
- Shows a link to download a pdf file