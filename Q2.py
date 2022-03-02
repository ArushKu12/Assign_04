# iterative method

from math import factorial

input=int(input("Enter the number of rows: "))

for i in range(0, input):
    for j in range(0, input - 1 - i):
        print(" ",end=" ")
    for k in range(0,i+1):
        print(factorial(i)/(factorial(k)*factorial(i-k)),end="  ")
    print("\n")

print("Question 2")
print()

print("Using recursion. \n")


def pascal_triangle(n, list1):
    if n == 0:
        return

    pascal_triangle(n - 1, list1)

    l = len(list1)
    list2 = list1.copy()
    list1.append(1)

    for counter in range(0, l):
        if counter == 0:
            list1[0] = 1
        else:
            list1[counter] = list2[counter] + list2[counter - 1]

    proper_pattern(list1)


def proper_pattern(list1):
    print(" " * (number - len(list1)), end="")

    for item in list1:
        print(item, end=" ")
    print()


number = int(input(f"Enter the number (natural number) of lines to print: "))
print()

initial_list = []
pascal_triangle(number, initial_list)