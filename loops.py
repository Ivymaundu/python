# for loops
# for i in range(0,15):
#   if i % 2 == 0:
#    print(i)

# write a for loop to print numbers from 1 to 5
# for i in range(1,6):
#     print(i)


# sum all the elements in a list using a for loop numbers = [2,3,4,5,6,7,8,9]
# numbers = [2,3,4,5,6,7,8,9]
# sum = 0
# for i in numbers:
#   sum+=i
# print(sum)

# ls = tuple(range(20,61))
# res = []
# for i in ls:
#   if i%7==0:
#     res.append(i)
#   else:
#     pass
# print(res)

# store only the first odd numbers between 0 and 50
num = list(range(0,51))
lis = []

# for i in num:
#   if i%2!= 0:
#     lis.append(i)
#     if len(lis)==10:
#       break
# print(lis)

# for i in num:
#   if len(lis) == 10:
#     break
#   if i%2!=0:
#     lis.append(i)
# print(lis)

count = 1
for i in num:
  if(i%2!=0):
    print(i)
    count=count+1
    if count==11:
      break
  else:
    pass
