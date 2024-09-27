# a = 1
# b = 1000
a, b = int(input("min = ")), int(input("max = "))
q = 0
while b >= a:
    m = (a+b) // 2
    q = q + 1
    x = input(f"question number {q}.. is your number {m}? (y or n) ")
    if x == 'n':
        z = int(input("Is your number bigger(2) or smaller(1)?"))
        if z == 1:
            b = m - 1
        elif z == 2:
            a = m + 1
    elif x == 'y':
        print(f" I win :-) with {q} questions")
        break
