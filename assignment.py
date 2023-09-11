#. Test how long your program takes to loop through 10,000 values, against 10,000,000.

# import timeit

# code_to_measure = """
# for i in range(10000):
#     pass
# """
# execution_time_1 = timeit.timeit(code_to_measure, number=10000)
# print("Time taken1: ",execution_time_1 ,"Seconds")


# code_to_measure = """
# for i in range(10000000):
#     pass
# """

# execution_time_2 = timeit.timeit(code_to_measure, number=10000000)
# print("Time taken2: ",execution_time_2 ,"Seconds")

# duration_taken = execution_time_2 - execution_time_1
# print("Duration",duration_taken ,"Seconds" )


import time

starting_time_1=time.time()
for i in range(10000):
    pass
ending_time_1=time.time()
time_taken_1=ending_time_1-starting_time_1

starting_time_2 = time.time()
for i in range(10000000):
    pass
Ending_time_2 = time.time()

time_taken_2 = Ending_time_2-starting_time_2

total_time_taken= Ending_time_2 - starting_time_2


print(total_time_taken)


# Create a list with random values and sort the list in ascending order, without using .sort.

my_list = [10,15,12,9,6,8,30]
print(my_list)

for num in range(0,len(my_list)):
    for next_num in range(num+1,len(my_list)):
        if my_list[num]>=my_list[next_num]:
            my_list[num],my_list[next_num] = my_list[next_num],my_list[num]

print(my_list)

#Generate numbers between 1000 and 10,000 and write only the numbers divisible by 7 in a .txt file

my_num = str([num for num in range(1000,10000) if num%7==0 ])
print(my_num)

text_file = open("myfile.txt","w")
L = my_num
 
text_file.writelines(L)
text_fileun.close() #to close file access mode