#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(5)
my_list.append(80)
my_list.append(4)
my_list.append(0)
my_list.append(10)

print(my_list)
my_list.print_sorted()
print(my_list)
