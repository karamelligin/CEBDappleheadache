# let us start all over again
import decimal


x = 10
home = "banana"
variable_name = "tina"

print(x)
print(home, "don\'t")
print(x, "home", home, variable_name.title())

a = "home "
b = "base"
c = a + " " + b
print(c)
d = a * 5
print(d)

print("Gas price is {0:2d},and cost per liter is :{1:6.2f}".format(12, 00.546))
y = 24.3
x = 23.9857
print(str(x))
print(int(x))
print(float(x))
print(decimal.Decimal(y))
print(len(b))
print('*', end="")
print('*')
print(b[1:4])
print(b[-1])
print(9/3, 9 % 3)
first_number = int(input("\nFirst Number: "))
divisible_number = int(input("\nDivisible By: "))

if first_number % divisible_number == 0:
    print("True")
else:
    print("False")
