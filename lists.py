cars = ["ford","audi","BMW","toyota","mazda",1,"subaru","tesla"]
print(cars)
week = ["monday","friday","wednesday","tuesday","thursday"]
print(week[3])

name = ["ivy","angie"]
cars = ["mike","kal"]
fruits=["ken","kim"]
name.remove("ivy")
# name.extend(cars),name.extend(fruits)
print(name)
# print("hello"+name)
# email = input("enter email")

# cars = ["volvo","ford",["toyota","mercedes",["mazda","subaru"]],"audi"]
# del(cars)
# cars.clear()
# cars.insert(1,"ivy")
# print(cars)

# car1 = input("Enter car name:")
# car2 = input("Enter car name:")
# car3 = input("Enter car name:")
# models=[]
# models.append(car1),models.append(car2),models.append(car3),
# models.remove("bmw")
# # del(models)
# models.clear()
# print(models)

# print(cars[2][2].insert(1,"t"))

trainees = ["John", [2, ["James","Mary"]]]

# 1. Display 2 from the list.
print(trainees[1][0])
# 2. Output James  from the list.
print(trainees[1][1][0])
# 3. Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)
# 4. Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,"Mike")
print(trainees)
# 5. Change the value of 2 to 8
trainees[1][0]=8
print(trainees)
# 6. Remove John and Mary from the list.xyyyg
# trainees[1][1].remove("Mary")
del(trainees)[0]
del(trainees)[0][1][2]
print(trainees)

# 7. Using a function, determine the length of the list
print(len(trainees))

cars = {"Name":"ivy", "age":12}
# print(cars[3])

cars = ["ford","bmw"]

print("ford" not in cars)
