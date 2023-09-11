#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(20)
my_list.append(4)
my_list.append(0)

print(my_list)
my_list.print_sorted()
print(my_list)
