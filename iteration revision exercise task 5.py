#Callum Brown
#21-10-14
#Exercise 5

total = 0
number = 0
count = 0

while number >= 0:
    number = int(input("Please enter a number: "))
    
    if number >= 0:
        total = total + number
        count = count + 1
average = total/count
print(average)
