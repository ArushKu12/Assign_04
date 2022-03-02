print("question number 6\n")
george_word = input("Enter the word uttered by George\n:-")
barbie_word = input("Enter the word mad up by barbie\n:-")
list_goerge_word = list(george_word)
list_barbie_word = list(barbie_word)
empty_list = []

for character in list_goerge_word:
    if character not in list_barbie_word:
        empty_list.append(character)

if len(empty_list) == 0:

    while True:

        check = input("Does the word made by barbie have any meaning? (enter Y or N)").upper()
        if check == "Y":

            print("Congratulations!!! your friendship is real")
            break

        elif check == "N":
            print("OOPS!! your friendship is fake ...stay away from each other ")
            break
        else:
            print("Enter the correct input")

else:
    print("OOPS!! your friendship is fake ...stay away from each other ")