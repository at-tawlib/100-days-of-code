student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
student_count = 0
for student_height in student_heights:
    sum += student_height
    student_count += 1
average = sum / student_count
print(round(average))





