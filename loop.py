# -*- coding: utf-8 -*-

fruits = ['Mango', 'Banana', 'Lichi', 'Grape']

# for loop
for x in fruits:
    print(x)
    
    

# break
for x in fruits:
    print(x)
    if x == 'Banana':
        break
    
    

# continue
for x in fruits:
    if x == 'Banana':
        continue
    print(x)
    
    

sum = 0

for x in range(0, 11, 2):
    sum = x + sum
print(sum)



# nested loop
fruits = ['Mango', 'Banana', 'Grape']
color = ['red', 'blue', 'green']

for x in fruits:
    for y in color:
        print(x,y)
        


# while loop
x = 0        
while x <= 10:
    x += 1
    if x == 5:
        continue
    
    print(x)


    