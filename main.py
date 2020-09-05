# Author: Alexander Barr ajb7463@psu.edu
letter1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
if letter1 == "A":
  grade1 = 4.0
  print("Grade point for course 1 is: 4.0")
elif letter1 == "A-":
  grade1 = 3.67
  print("Grade point for course 1 is: 3.67")
elif letter1 == "B+":
  grade1 = 3.33
  print("Grade point for course 1 is: 3.33")
elif letter1 == "B":
  grade1 = 3.0
  print("Grade point for course 1 is: 3.0")
elif letter1 == "B-":
  grade1 = 2.67
  print("Grade point for course 1 is: 2.67")
elif letter1 == "C+":
  grade1 = 2.33
  print("Grade point for course 1 is: 2.33")
elif letter1 == "C":
  grade1 = 2.0
  print("Grade point for course 1 is: 2.0")
elif letter1 == "D":
  grade1 = 1.0
  print("Grade point for course 1 is: 1.0")
else:
  grade1 = 0
  print("Grade point for course 1 is: 0.0")
letter2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if letter2 == "A":
  grade2 = 4.0
  print("Grade point for course 2 is: 4.0")
elif letter2 == "A-":
  grade2 = 3.67
  print("Grade point for course 2 is: 3.67")
elif letter2 == "B+":
  grade2 = 3.33
  print("Grade point for course 2 is: 3.33")
elif letter2 == "B":
  grade2 = 3.0
  print("Grade point for course 2 is: 3.0")
elif letter2 == "B-":
  grade2 = 2.67
  print("Grade point for course 2 is: 2.67")
elif letter2 == "C+":
  grade2 = 2.33
  print("Grade point for course 2 is: 2.33")
elif letter2 == "C":
  grade2 = 2.0
  print("Grade point for course 2 is: 2.0")
elif letter2 == "D":
  grade2 = 1.0
  print("Grade point for course 2 is: 1.0")
else:
  grade2 = 0
  print("Grade point for course 2 is: 0.0")
letter3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))
if letter3 == "A":
  grade3 = 4.0
  print("Grade point for course 3 is: 4.0")
elif letter3 == "A-":
  grade3 = 3.67
  print("Grade point for course 3 is: 3.67")
elif letter3 == "B+":
  grade3 = 3.33
  print("Grade point for course 3 is: 3.33")
elif letter3 == "B":
  grade3 = 3.0
  print("Grade point for course 3 is: 3.0")
elif letter3 == "B-":
  grade1 = 2.67
  print("Grade point for course 3 is: 2.67")
elif letter3 == "C+":
  grade3 = 2.33
  print("Grade point for course 3 is: 2.33")
elif letter3 == "C":
  grade3 = 2.0
  print("Grade point for course 3 is: 2.0")
elif letter3 == "D":
  grade3 = 1.0
  print("Grade point for course 3 is: 1.0")
else:
  grade3 = 0
  print("Grade point for course 3 is: 0.0")
final = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3)  
print(f"Your GPA is: {final}")