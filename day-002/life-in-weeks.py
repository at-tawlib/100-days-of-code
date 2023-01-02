age = input("What is your current age? ")

age_as_int = int(age)
remaining_years = 90 - age_as_int
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")