#Creating a file called myfile.txt
f=open('myfile.txt ','w')
str="This is a sample test text. Regarding python exceptions"

f.write(str)

#ask the user to input a file name
try:
	name=input("Enter filename")
	f=open(name,'r')

except IOError:
	print("File not found ")
else:
	strr=f.read()
	print(strr)	
f.close()

# to raise and handle exceptions

# TypeError

a = 5
b = '6'
try:
    sum = a + b
except TypeError as e:
    print("Type Error has occurred: {}".format(e))
else:
    print('Quotient : {}'.format(sum))
finally:
    print("Maths is fun!")

# NameError

try:
    print(answer)
except NameError as e:
    print("Name Error has occurred : {}".format(e))
except Exception:
    print('Something went wrong!')
else:
    print('No errors!')

# raising a KeyboardInterrupt

try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print('There is a KeyboardInterrupt!')
finally:
    print("No interrupts are allowed!")

# IndexError

try:
    list = [1, 2, 3, 4]
    print(list[4])
except IndexError:
    print("Index Error raised. List index is out of range")
else:
    print('No error!')

# FileNotFoundError

try:
    f = open("file1.cat", "r")
except FileNotFoundError:
    print("File not Found!")

# ZeroDivisionError and ValueError

x = input("Enter Dividend : ")
y = input("Enter Divisor : ")
try:
    result = int(x) / int(y)
except ZeroDivisionError:
    print("You cant divide by zero!")
except ValueError:
    print("Invalid Input. Enter numbers only!")
else:
    print(result)
