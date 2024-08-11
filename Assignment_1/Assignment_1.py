#1.  The following line won't run because of a syntax error 
#    print("hi)

print('hi')



#2.  Exercise 2
#''' The following lines won't run properly,
#   even if the syntax error in the line above is corrected,
#    because of a run-time error '''
#print(hello)


hello='Hi, Good Morning'
print(hello)



#3.  Display a string (greeting message) directly 
print('Hey, Good Morning')



#4. Display the contents of a string variable
a='Hello'
print(a)



#5. Display the string which contains single quotes 
#     Ex: Indian's
print("Indian's")



#6. Display the string which contains Double Quotes 
#Ex: Students,"Welcome to SOIS".
print('Students,"Welcome to SOIS"') 



#6. Read two numbers in (user input) and store as num1 and num2, Calculate the sum, difference, product, Quotient, reminder, power
num1=int(input())
num2=int(input())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)



#7. check the value of num1 is integer or not? 

num1 = 20
if isinstance(num1, int):
    print(num1, 'is an integer')
else:
    print(num1, 'is not an integer!!')
     


#8. convert into integer
a=input()
print(type(a))
b=int(input())
print(type(b))
print(b)

  
#9. Find the datatype for the variable num1 and num2.
a=10.0
b='Hello'
print(type(a))
print(type(b))  



#10. read the float value from the user and print the number rounded to 2 decimal places
number=float(input())
print(round(number,2))



#11. read the float value from the user and print the absolute value 
number = float(input("Enter a float value: "))
absolute_value = abs(number)
print(absolute_value)



#12. Store different type values in the variable 

#String 
my_string = "Hello, World!"
print("String:", my_string)

#numeric
my_integer = 42
my_float = 3.14
print("Integer:", my_integer)
print("Float:", my_float)

 
#complex 
my_complex = 2 + 3j
print("Complex:", my_complex)

#list 
my_list = [1, 2, 3, "four", 5.0]
print("List:", my_list)


#dictionary 
my_dict = {
    	"name": "Alice",
    	"age": 30,
    	"city": "Mangalore"
	}
print("Dictionary:", my_dict)

#set 

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

#tuple 

my_tuple = (10, 20, 30, "forty")
print("Tuple:", my_tuple)




#13. Find the data type for the above variables 
print("Data Type of my_string:", type(my_string))
print("Data Type of my_integer:", type(my_integer))
print("Data Type of my_float:", type(my_float))
print("Data Type of my_complex:", type(my_complex))
print("Data Type of my_list:", type(my_list))
print("Data Type of my_dict:", type(my_dict))
print("Data Type of my_set:", type(my_set))
print("Data Type of my_tuple:", type(my_tuple))



#14. Display the number of letters in the string
greeting = "Welcome to Python Programming"
print(len(greeting))         #(including spaces)
print(len(greeting.replace(" ","")))



#15. read the first name and last name from the user and combine first name and last name. combine name and greeting message
a=input()
b=input()
full_name=a+" "+b
print('Hi ',full_name)



#16. Display the string with space 
#    Ex: firstname lastname 
firstname=input()
lastname=input()
full_name=firstname+" "+lastname
print('Hi ',full_name)



#7. Display first two characters from the name 

a=input()
print(a[:2])



#18. Display last three characters from the name 
a=input()
print(a[-3:])



#19. Display 3rd character to last character 
a=input()
print(a[2:])


#20. Display 3rd to 5th character 
a=input()
print(a[2:5])



#21. Create a list of food with two elements. 	
lst=['Idli','Dosa']
print(lst)



#22. Add one more to the food list using .append()

lst=['Idli','Dosa']
print(lst)
lst.append('Parotta')
print(lst)
	


#23. Add two more food strings to food using .extend()

lst1=['Idli','Dosa']
print(lst1)
lst2=['Bread','Bun']
print(lst2)
lst1.extend(lst2)
print(lst1)



#24. Count total number of items in the list 
lst1=['Idli','Dosa','Poori','Chapathi','Sandwich']
print(len(lst1))
	


#25. Print the first two items in food using slicing notation
lst1=['Idli','Dosa','Poori','Chapathi','Sandwich']
print(lst1[0:2])



#26. Print the last item in food using index notation
lst1=['Idli','Dosa','Poori','Chapathi','Sandwich']
print(lst1[-1])
	

#27. Debug: Program is to check the given number is odd or even 

number = int(input("Enter a number: "))
x = number%2
if x == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")



#28. Debug: Program is to convert centigrade to Fahrenheit
c = float(input("Enter temperature in Centigrade: "))
f = 9*(int(c))/5 +32
print("Temperature in Fahrenheit is: ",f)



#29. Debug: 

count = int(input("Enter the count of numbers: "))
i = 0
summ= 0
for i in range(count):
    x = int(input("Enter an integer: "))
    summ = summ + x
avg = summ/count

print("The average is: ", avg)



#30. Prove : strings is not mutable 
#            lists are mutable 

str='HelloWorld'
str[0]='A'		#(Gives Error since it is not mutable)
print(str)

lst=['CSE','CYS','BDA','VLSI']
lst[0]='AIML'
print(lst)		#(Since lst are mutable the first element is replaced with new element)

	

