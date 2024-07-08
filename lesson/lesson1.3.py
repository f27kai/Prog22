"""
    ТЕМА: цикл while
"""

# i = 2
#
# while i <= 32:
#     i *= 2
#     print(i)


i = 1

while i < 11:
    j = 0
    while j < 11:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    print()


# while True:
#     age = input("Жашыныз канчада? ")
#
#     if age == "выход":
#         print("Finished ...")
#         break
#
#     age = int(age)
#
#     if age >= 16:
#         print("Паспорт алууга уруксат")
#     else:
#         print("Тилекке каршы паспорт берилбейт")
#     print()
