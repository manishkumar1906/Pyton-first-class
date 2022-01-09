#introduction to modules-os,shutil
import os
# display date and time from os
#os.system('date')

#creating new folder using os
#os.mkdir('C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file2')

#check current working directory
os.getcwd()

path='C:/Users/Sonakshi/Desktop'
#check wether the specified path exists or not
print (os.path.exists(path))


path = 'C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file1.txt'
#split the path in route and extension pair
root=os.path.splitext(path)
print('root path= ',root[0])
print('extension= ',root[1])

#list all file and folder using os
os.listdir()

import shutil
path = 'C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction'
print ('before coping file')
print (os.listdir(path))
source='C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file1.txt'
destination = 'C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file3.txt'
#copy the content source to destination
dest = shutil.copy(source,destination)
print ('after coping file')
print (os.listdir(path))

path = 'C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction'
print ('before moving file')
print (os.listdir(path))
source='C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file1.txt'
destination = 'C:/Users/Sonakshi/Desktop/New folder/python/Python Introduction/file3.txt'
#moving the content source to destination
dest = shutil.move(source,destination)
print ('after moving file')
print (os.listdir(path))