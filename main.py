import random
num=random.randint(1,10)
guess=int(input('please guess the number? '))
while num !=guess:
    guess=int(input('uffs !! try again :guess again:'))
else:
    print('congratulations!!! you are right')