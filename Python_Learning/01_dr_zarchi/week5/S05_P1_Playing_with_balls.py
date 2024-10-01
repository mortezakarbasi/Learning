n = int(input("Enter your balls numbers? "))
if n % 3 == 0:
    print("I'm the second player")
else:
    print("I'm the first player")
    m = n % 3
    print(f"I will pick up {m} balls")
    n = n - m
while n > 0:
    print(f"There are {n} balls on table")
    m = int(input("How many balls do you want to pick up? "))
    if m != 1 or m != 2:
        print("you have to pick up 1 ball or 2 balls.")
        continue
    n = n - m
    m = n % 3
    print(f"I will pick up {m} balls")
    n = n - m
print("There are't any balls on table! ")
print("I'm winner ! HHHHH")
