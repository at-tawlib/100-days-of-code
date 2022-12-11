# Day 028 - Tkinter, Dynamic Typing and the Pomodoro GUI Application
## Pomodoro Project
- The app applies the pomodoro technique 
- 25min work => 5min break => 25min work => 5min break => 25min work => 5min break => 25min work => 20min break
- i.e. 4 sets of 25minutes with 5 minutes interval

### Steps
- Setup the UI
- Put the image in the UI
- Put the text [timer] on the image using canvas
- Add labels at top and buttons below
- Add a countdown mechanism
- Create a function for the start button to start the timer
- Format the counter to output time in minutes not in seconds
- Use the reps variable to count down the appropriate number of seconds.
- When the program is run, the timer switches between counting down the work time and the break time
- During long break  = Break in red, short break  = break in pink, work time  = Work in green
- Show the checkmark when the user has completed a work session 