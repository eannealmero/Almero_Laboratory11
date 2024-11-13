# input 5 student grade and identify:
# average grade:
# number of students with passing grade:
# passing percentage:
# display grades
# passing grade is 75 and above
# grade input must be between 40-100

students = 5
counter = 0
passed = 0 
grades=[]


for grade in range(5):
    x = int(input("Enter students' grade: "))
    if 40 <= x <= 100:
        grades.append(x)
        counter += 1
        if x >= 75:
            passed += 1
        
    else:
        print("Invalid grade input. It is not between 40-100.")
        break


if counter == 5:
    average_grade = sum(grades) / 5        
    passing = (passed / 5) * 100
    rounded_passing = round(passing, 2)
    

    print (f"Average of all grades: {average_grade}")
    print (f"Number of people who passed: {passed}")
    print (f"Percentage of people who passed: {passing}%")
    print (f"Grades input include: {grades}")

else:
    print("The program stopped due to an error. Please check your grade input.")

