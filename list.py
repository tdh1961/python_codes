my_list = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]

#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(), .count()

print(len(my_list))

my_list.append('Houston') #  .append will only add one item to the list
print(my_list)

my_list.pop()
print(my_list)

my_list[0]='Terraform'
print(my_list)
print(my_list[2].upper())

my_list.extend([10,56,78]) #.extend will add many items at the same time to my list
print(my_list)
print(dir(list))
my_list.insert('1, huguette')
print(my_list)



