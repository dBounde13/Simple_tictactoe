grades = input().split(" ")   # put your python code here
new_grades = [grade for grade in grades if grade.startswith("A")]
a = len(grades)
b = len(new_grades)
c = b / a
print(round(c, 2))
