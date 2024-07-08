""""
    ТЕМА: if elif else
"""

# age = int(input("Жашыныз канчада? "))
#
# if age >= 16:
#     print("Паспорт алууга уруксат")
# else:
#     print("Тилекке каршы паспорт берилбейт")


x = int(input("x: "))
option = input("+, -, /, *    ")
y = int(input("y: "))

if option == "+":
    print(x + y)
elif option == "-":
    print(x - y)
elif option == "/":
    if y == 0:
        print("Infinity")
    else:
        print(x / y)
else:
    print(x * y)


