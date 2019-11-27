#7. functions
#==================================
#Python Function
#----------------------------------		
#In Python, function is a group of related statements that perform a specific task.
#Functions help break our program into smaller and modular chunks. 
#As our program grows larger and larger, functions make it more organized and manageable.

# Syntax of Function
# ===========================================
# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)

def Hello():
	""" Example of Function or Method """
	print("This is my fitst function")
	print("Created by me")
	print("Thank you very much")

#calling function	
##Hello()
	
def SayHello(n):
	""" Example of Function or Method """
	print("This is my second function")
	print("Created by {}".format(n))
	print("Thank you very much")

#myname = input("Enter your name : ")
#SayHello(myname) #Arguments

def FullName(a,b):
	print("Hello Mr.%s %s" % (a,b))
	print("Hello Mr.{1} {0}".format(a,b))
	
#FullName('Chand','Miah')
	
def ShowFullName(a,b):
	return "Hello Mr.{1} {0}".format(a,b)
	
#x =ShowFullName('Moon','Sweet Heart')
#print(x)
#print(ShowFullName('Moon','Sweet Heart'))
	
def Add(a,b):
	return a+b
	
#print(Add(5,2))	
	
#Python Arbitrary Arguments
def greet(*names):
	for x in names:
		print(x)

#greet("Munaz","Hridita","Moon")

def AddNums(*nums):
	jog=0
	for x in nums:
		jog = jog + x
		
	print(jog)
	
#AddNums(3,1)	

def getNums(*nums):
	jog=0
	for x in nums:
		jog = jog + x
		
	return jog
	
#print(getNums(3,1)	)

def multi(x):
	return x*x
	
#print(multi(3))	

# Anonymous Function
# lambda arguments: expression
res = lambda x: x * x

#print(res(5))

#Keyword Arguments
#---------------------
#describe_pet(animal_type='hamster', pet_name='harry')
def displayPet(o,p):
	print("{} {}".format(o,p))

#displayPet("Moon","Cat")
#displayPet(p="Cat",o="Moon")

#Default Values
#-----------------
def SHOWPet(o="Nazmul",p="Tiger"):
	print("{} {}".format(o,p))

SHOWPet()
SHOWPet("Cat")
SHOWPet("Moon","Cat")
#passing list
def greet_users(names):
	for i in names:
		print(i)

mylist = ["Sahdat","Moon","Nazmul","Dipu"]
greet_users(mylist)

def print_kwargs(**kwargs): #parameter dict type
    print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
#output {'kwargs_3': True, 'kwargs_2': 4.5, 'kwargs_1': 'Shark'}

def myKey_Args(**x):
	for k,v in x.items():
		print(k,v)
	
myKey_Args(x1="Shark", x2=4.5, x3=True)	

def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(my_name="Sammy", your_name="Casey")
