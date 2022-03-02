# Tower of hanoi problem

# helper is the rod used to transfer disc
# destination is where all the disc finally be placed
def hanoi_tower(n, source, helpr, destination):
    # source is where all the disc are kept initially

    if n == 1:

        print(f"move disc 1 from {source} to {destination}")

        return

    hanoi_tower(n - 1, source=source, helpr=destination, destination=helpr)

    print(f"move {n} disc from {source} to {destination}")

    hanoi_tower(n - 1, source=helpr, helpr=source, destination=destination)



number = int(input("Enter the number of discs: "))

hanoi_tower(number, "A", "B", "C")
