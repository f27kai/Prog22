"""
    ТЕМА: цикл for
"""
#
# world = "Hello"
#
# for i in world:
#     print(i)

#
# for i in range(1, 101):
#     print(i)
#
# for i in range(101):
#     print(i)


# for i in range(1, 506, 15):
#     print(i)

# for i in range(1,11):
#     for j in range(11):
#         print(f"{i} * {j} = {i * j}")
#     print()


# for i in range(1, 11):
#     if 5 == i:
#         continue
#     print(i)


world = input("Enter your text: ")

russian = "АаОоУуИиЭэЕеЁёЮюЯя"
english = "AaEeIiOoUuYy"

vowels = 0
consonants = 0

for i in world:
    if i in russian:
        vowels += 1
    elif i in english:
        vowels += 1
    else:
        consonants += 1

print(f"Vowels: {vowels}\n"
      f"consonants: {consonants}")
