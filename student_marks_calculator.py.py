name = input("Enter Student name: ")
Standard = input("Enter class name: ")

python_marks = int(input("Enter Python Marks: "))
java_marks= int(input("Enter Java Marks: "))
C_marks= int(input("Enter C Marks: "))
html_marks= int(input("Enter Html Marks : ")) 

total = python_marks + java_marks + C_marks + html_marks 
percentage = (total / 400) *100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"


print("\n-----Student result-----")
print("Student name:",name)
print("Class:",Standard)
print("Python_marks:",python_marks)
print("Java_marks:",java_marks)
print("C_marks:",C_marks)
print("Html_marks:",html_marks)
print("Total_marks:",total)
print("Percentage:",percentage)
print("Grade:",grade)