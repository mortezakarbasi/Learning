A = [[0] * 3 for i in range(3)]


# fill table with number 1 to 9
def init_table(A):
    Kooneh = 1
    for i in range(3):
        for j in range(3):
            A[i][j] = Kooneh
            Kooneh = Kooneh + 1


def print_table(A):
    for i in range(3):
        for j in range(3):
            print(A[i][j], end=" ")
        print()
    print()


print_table(A)
init_table(A)


def Put(x, s):
    row = x // 3
    column = x % 3
    if A[row][column] == "X" or A[row][column] == "O":
        print("Jerzani!!! :-(  (0___0) ")
        exit(0)
    A[row][column] = s


def Check(s):
    for i in range(3):
        if A[i][0] == s and A[i][1] == s and A[i][2] == s:
            return True
        if A[0][i] == s and A[1][i] == s and A[2][i] == s:
            return True
        if A[0][0] == s and A[1][1] == s and A[2][2] == s:
            return True
        if A[0][2] == s and A[1][1] == s and A[2][0] == s:
            return True
        return False


for move in range(9):
    if move % 2 == 0:
        x = int(input("player 1(X): "))
        Put(x-1, "X")
        if Check("X"):
            print("Player 1 win! ")
            break
    else:
        x = int(input("player 2(O): "))
        Put(x-1, "O")
        if Check("O"):
            print("Player 2 win! ")
            break

    print_table(A)
