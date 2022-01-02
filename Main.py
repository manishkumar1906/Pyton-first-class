print('hii happy new year')

## single line comment
"""
multi-line
comment 
"""

# datatypes
#number-> int(whole number) float(decimal number)
a = 10
print(type(a)) # <class 'int'>

b = 10.4444
print(type(b)) # <class 'float'>

sum = a+b
sub = a-b
divide = a/b 
mul = a*b
rem = a//b 


#string-> str "string"
string = "Happy New Year"
#concatination or concat
output = "hello"+"manish"
concat = "link"+string+".mp3"
print(output)
print(concat)


#boolean-> bool- True False
a = True
print(type(a)) #<class 'bool'>


#list-> [] index and values. index starts form 0.its just like arrays
lst = [2,"Manish","Python",1]

#tuple-> ()
#dictonary->{key:value}

#taking input from user
age = input ('enter your age ')
print ( type (age))
age = int (input('enter your age'))
print ( type (age))
#if condition to check if a person in eligble to vote
if (age > 18 ):
    print ('you are an adult you can vote')
elif (age <= 13 ):
    print ('you are a child you cannot vote')
else :
    print ('you are a teenager')



#program to count the words 
string = input('enter your introduction: ')
print(string)
charcount = 0
wordcount = 0
for i in string :
    charcount=charcount+1
    if (i==' '):
        wordcount=wordcount+1
print (charcount)    
print('number of words in the string is ',wordcount)