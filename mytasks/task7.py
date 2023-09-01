# Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 

mark = float(input("Enter students' mark: "))

if mark>79 and mark<100:
    mark = "A"
elif mark>=60 and mark<=79:
    mark = "B"
elif mark>=49 and mark<=59:
    mark = "C"
elif mark>=40 and mark<=49:
    mark = "C"
elif mark>0 and mark<40:
    mark = "E"
else:
    mark = "Invalid marks"
print(mark)