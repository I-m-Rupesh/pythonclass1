# file open  --> name , mode : r ,  w , a , x
# file modification
# file close

# to create file 
#f = open('sample.txt', 'x')  

# to write content in the file
f = open('sample.txt', 'w')
content = input('Enter text to write in file')
f.write(content)
f.close()

# to read  content from the file
f = open('sample.txt', 'r')
print(f.read())
f.close()

# to append content in the file
f = open('sample.txt', 'a')
content = input('Enter text to write in file')
f.write(content)
f.close()

f = open('sample.txt', 'r')
print(f.read())
f.close()