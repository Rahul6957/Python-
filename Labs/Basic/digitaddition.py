#Write a Python program to calculate the sum of digits of a number.


s1=(input("Enter No:"))
sum=0
for i in s1:
    sum=sum + int(i)
print(sum)