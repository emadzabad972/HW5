# start

height: float= float(input('height? '))

while height < 0.4 or height > 2.5:
    print("wrong input!")
height = float(input('whats your height?'))

# end
print()

# start

num_1: int = int(input('enter first number: '))
num_2: int = int(input('enter second number: '))
if num_1 < num_2:
    for i in range(num_1, num_2 + 1, 1):
        print(i, end=" ")
else: # num_2 <= num1
    for i in range(num_1, num_2 -1, -1):
        print(i, end=" ")

# end
print()
# start

counter: int = 1

pie: float = float(input('enter the value of pie: '))

while pie != 3.14 and counter < 3:
    print('try again')
    counter += 1
    pie = float(input('enter the value of pie: '))
if pie == 3.14:
  print("you are correct")
else:
   print("pie is 3.14!")
#end
print()
# start

while True:
    num_1: int = int(input('enter first number: '))
    num_2: int = int(input('enter second number: '))
    num_3: int = int(input('enter third number: '))
    if 0 <= num_1 <= 10 <= num_2 <= 60 <= num_3 <= 100 and num_2 == (num_1 + num_2 + num_3) / 3:
        break



