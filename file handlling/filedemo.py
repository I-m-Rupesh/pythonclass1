# file open  --> name , mode : r ,  w , a , x
# file modification
# file close



f = open('sample.txt', 'w')
content = input('Enter text to write in file')
f.write(content)
f.close()

f = open('sample.txt', 'r')
print(f.read())
f.close()

f = open('sample.txt', 'a')
content = input('Enter text to write in file')
f.write(content)
f.close()

f = open('sample.txt', 'r')
print(f.read())
f.close()