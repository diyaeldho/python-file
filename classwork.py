# def factorial(n):
#     result =1
#     for i in range(1,n+1):
#         result = result *i
#     return result 
# num= int(input("Enter a number: "))
# print("factorial=", factorial(num))

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         return True
# num= int(input("Enter a number:"))
# print(is_prime(num))

# def count_vowels(text):
#     count =  0
#     for ch in text:
#         if ch in "aeiouAEIOU":
#             count+=1
#     return count
# text=input("Enter a string:")
# print("Number of vowels =", count_vowels(text))

# def reverse_string(text):
#     return text[::-1]
# text = input("Enter a string:")
# print("Reverse =", reverse_string(text))

# def is_palidrome(text):
#     if text== text[::-1]:
#         return True
#     else:
#         return False
# text=input("Enter a string:")
# print(is_palidrome(text))

# def list_sum(numbers):
#     total =0
#     for num in numbers:
#         total= total+num
#     return total
# numbers=[10,20,30,40]
# print("total =",list_sum(numbers))

# def find_largest(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if num>largest:
#             largest= num
#     return largest
# numbers=[10,45,50,12,80]
# print("largest=", find_largest(numbers))

# def count_even(numbers):
#     count=0
#     for num in numbers:
#         if num%2==0:
#             count+=1
#     return count
# numbers=[10,15,20,25,30]
# print("Even number=", count_even(numbers))

# def multiplication_table(n):
#     for i in range(1,11):
#         print(n,"x",i,"=",n*i)
# num= int(input("Enter a number:"))
# multiplication_table(num)

# def calculate_result(mark1, mark2, mark3):
#     average = (mark1+mark2+mark3)/3
#     if average>=50:
#         return"pass"
#     else:
#         return"fail"
# m1 = float(input("Enter mark1:"))
# m2 = float(input("Enter mark2:"))
# m3 = float(input("Enter mark3:"))
# print("Result =",calculate_result(m1,m2,m3))

# def is_disarium(number):
#     digits = str(number)
#     total =0
#     position =1
#     for digit in digits:
#         total=total+int(digit) **position
#         position= position+1
#     if total==number:
#         return True
#     else:
#         return False
# number= int(input("Enter a number:"))
# if is_disarium(number):
#     print(number,"is a disarium number.")
# else:
#     print(number,"is not a disarium number.")

# def reverse_vowels(s):
#     vowels = "aeiouAEIOU"
#     s=list(s)
#     left = 0
#     right=len(s)-1
#     while left<right:
#         if s[left] not in vowels:
#             left+=1
#         elif s[right] not in vowels:
#             right-=1
#         else:
#             s[left],s[right]=s[right],s[left]
#             left+=1
#             right-=1
#     return "".join(s)
# s=input("Enter a string:")
# print(reverse_vowels(s))

# strs = ["apple","app","applications"]
# prefix = ""
# for i in range (len(strs[0])):
#     for word in strs:
#         if i >= len(word) or word[i] !=strs[0][i]:
#             print(prefix)
#             exit()
#     prefix += strs[0][i]
# print(prefix)

# for i in range(1,6):
#     for j in range(i):
#         print(chr(64 + i), end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(1,12):
#     for j in range(i):
#         print(int(0+i),end=" ")
#     print()

# for i in range(1,6):
#     a=i
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print()

# l=[]
# num=int(input("Enter the number of num:"))
# for i in range(num):
#     number=int(input(f"enter your{i+1} number : "))
#     l.append(number)
# print(l)


# import random

# name=input("Enter your Name:")

# secret_number=random.randint(1,20)

# print("Welcome",name,"!")
# print("I have selected a number between 1 and 20.")
# print("You have 6 attempts to guess the number.")

# attempts=0

# while attempts<6:
#     guess=int(input("Enter your Guess:"))
#     attempts+=1

#     if guess<=secret_number:
#         print("Your guess is too low")
#     elif guess>=secret_number:
#         print("Your guess is too high")
#     else:
#         print("Congratualtion", name,"!")
#         print("You guess the corect number in",attempts,"attempts")
#         break
# if guess !=secret_number:
#     print("Game Over!")
#     print("The Correct answer was:",secret_number)

