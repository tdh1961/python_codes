import os

def hello():
    print('hello girl')
    print('how are you?')

def hello1(name):
    print(f'hello {name}')
    print('how are you?')

def command(cmd):
    
    os.system(cmd)

command('ls') # For every Linux command


def list_files(dir_path):
    

    for item in os.listdir(dir_path):
        path= os.path.join(dir_path, item)
        if os.path.isfile(path):
            print(f"{path}is a file")
        else:
            print(f"{path}is a directory")

list_files("/")

def add(a,b):
    return a+b

var_ =add(2,4)
print(var_)