import numpy as np
import statistics as stats

#1.finding the mean of this list 
lists = [20,22,50,35,66,78,99,22]

y = np.mean(lists)
print(y)

#2. What is the output? arr = np.arange(100,160,60)

arr = np.arange(100,160,60)
print(arr)

#3. Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5,] Find the mode value in this list using a function. *

Track = [4.1,5.1,4.5,4.9,5.6,7.5,8.5,]
x = stats.mode(Track)
print("This is the Mode value: " + str(x))

def mode_value(args):
    b = stats.mode(Track)
    return args + str(b)
print(mode_value("This is the Mode Value: "))

#5. What is the output for this code? print(2**3**3) *
print(2**3**3)

#8. Create a class function call phonebook? That prints out names and numbers.
class Phone_book:
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def numbers(self):
        print(self.name, str(self.number))

p1 = Phone_book("John", 782440907)

print(p1.name)
print(p1.number)

p1.numbers()

#9. Create a while loop that keeps adding the amount of grapes in hand 20 times.
