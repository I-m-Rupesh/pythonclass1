friendslist = ['Rohan', 'Bhavesh', 234, 87.4, True]
# print(type(friendslist))

user = (10,'Rupesh','python')
     
#print(type(user))


login =  ('Rupesh',1234)
user_dtl = user + login
# print(user_dtl[2:4])

#immutable --> it can not change
#user_dtl[2] = 'xyz'  this is not allowed 

# friendslist[2]= 'xyz'
# print(friendslist[2])
# print(len(user))
# print(len(user_dtl))

for i in user_dtl:
    print(i)

