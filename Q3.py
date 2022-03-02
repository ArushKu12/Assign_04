print("Question 3")
print()

# Question 3
num_1= int(input("Enter the first number:"))
num_2= int(input("Enter the second number (it should not be zero):"))
quotient_remainder = divmod(num_1,num_2)
print(f"quotient is {quotient_remainder[0]} remainder is {quotient_remainder[1]}")

# check whether function is callable or not

print("part a \n")

check = callable(divmod)

if check==True:

    print("its callable")

elif check==False:

    print("it is not callable")
print()
# part 2
print("part b \n")
if quotient_remainder[0]==0 and quotient_remainder[1]:
    print(f"quotient and remainder both are zero")
elif quotient_remainder[0]==0:
    print("quotient is zero")
elif quotient_remainder[1]==0:
    print("remainder is zero")
else:
  print("both are non zero")
print()
#part 3
print("part c \n")
list_qoutient_remainder=list(quotient_remainder)
additives=[4,5,6]
for i in additives:
    list_qoutient_remainder.append(i)
quotient_remainder=tuple(list_qoutient_remainder)
new_list=[]
for j in quotient_remainder:
    if j>4:
        new_list.append(j)
tup_newlist=tuple(new_list)
print(f"filtered out values are {tup_newlist} ")
print()
# question part 4
print("part d \n")
set_type=set(tup_newlist)
print(f"set data type is {set_type}")
print()
# question part 5
print("part e \n")
immutable_set=frozenset(set_type)
print("set is now immutable")
print()
# question part 6
print("part f \n")
print(f"max value of set is {max(set_type)}")
print(f"hash value is {hash(immutable_set)}")