# traffic light
#color = 'red' --> stop
#color = 'green' --> go
#color = 'yellow' --> slow

color = input("Enter \nred \nyellow \ngreen \n")
print("Selected colour = ", color)
if color == 'red':
    print("Stop")
elif color == 'green':
    print('Go')
elif color == 'yellow':
    print('Slow')
else:
    print("Wrong color selected")
print('End of code')