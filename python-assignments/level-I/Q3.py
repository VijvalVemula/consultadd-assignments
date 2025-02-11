"""
3. Write a Python program to input marks for five subjects Physics,
Chemistry, Biology, Mathematics, and Computer. Calculate the
percentage and grade according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
"""
print("Enter marks for the following subjects (out of 100):")
physics = float(input("Physics: "))
chemistry = float(input("Chemistry: "))
biology = float(input("Biology: "))
mathematics = float(input("Mathematics: "))
computer = float(input("Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 70:
    print("C")
elif percentage >= 60:
    print("D")
elif percentage >= 40:
    print("E")
else:
    print("F")