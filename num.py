#WAP a program to check a number given by the user is armstrong number.

num=int(input('enter the number'))
num_dublicate = num
sum =0
while num>0:
    rem=num %10
    cube_value=rem ** 3
    sum=sum+cube_value
    num=num//10
print(sum)
if sum == num_dublicate:
    print("it is a armstrong")
else:
    print("it is not armstrong")