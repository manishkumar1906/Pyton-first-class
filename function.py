#introduction to python function
#1 predefined functions - print(), input(), open(), split()
#open()- this can be used to read, write or append in a file
f= open('file1.txt')
#print (f.read())
filelines = f.readlines()
for i in filelines:
    print(i)
string = "My name is manish. I am 14 years old"
words = string.split ()
print (words)
print (string.split('m'))
print (string.split ("."))

#user defined functions
def functionname ():
    pass
#function definition
def greeting (name):
    print('Hello '+name+' .how are you')
#function called
greeting('manish')