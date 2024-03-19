...
f = open('test.txt' , 'w')   # 'w' , 'a' , 'r' this helps to write into the file
f.write('this is the first line\n')
f.write('this is the second line')
f.close 




with open('test.txt' , 'w') as f:     # in this case, the system withh "w" will overide what it is in the file for the new content.
    f.write('first line\n')   # "a" append mode will only add z new content to the file for the existing file
    f.write("second line\n")
f.close 

print(dir(f))
...
