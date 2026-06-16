
import time

my_list = ['apple', 'banana', 'orange', 'grape']
index = 0

#while True:
    #print(my_list[index % len(my_list)])
#    index += 1



start_time = time.time()

while True:
    print(my_list[index % len(my_list)])
    index += 1

    if time.time() - start_time > 10: # Stop after 10 seconds
        break