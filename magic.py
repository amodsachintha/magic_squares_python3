# https://github.com/amodsachintha/magic_squares_python3
N = 3


# sum horizontal axis
def sum_horizontal(square):
    h_sum = []
    row_sum = 0
    for x in range(N):
        for y in range(N):
            row_sum += square[x][y]
        h_sum.append(row_sum)
        row_sum = 0
    return h_sum


# sum vertical axis
def sum_vertical(square):
    v_sum = []
    col_sum = 0
    for x in range(N):
        for y in range(N):
            col_sum += square[y][x]
        v_sum.append(col_sum)
        col_sum = 0
    return v_sum


# sum diagonal axis
def sum_diagonals(square):
    d_sum = []
    diagonal_1 = 0
    diagonal_2 = 0
    for x in range(N):
        diagonal_1 += square[x][x]
        diagonal_2 += square[x][N - (x + 1)]

    d_sum.append(diagonal_1)
    d_sum.append(diagonal_2)
    return d_sum


# check if sums are equal in horizontal, vertical
# and diagonal arrays
def check_equal(iterator):
    return len(set(iterator)) <= 1


# method to find duplicates for lo shu condition
def find_repeat(square):
    seen = set()
    for x in range(N):
        for y in range(N):
            if square[x][y] in seen:
                return 0
            seen.add(square[x][y])
    return 1


# lo shu checks
def is_lo_shu(square):
    if sum(sum_horizontal(square)) == 45:
        if sum(sum_vertical(square)) == 45:
            if sum(sum_diagonals(square)) == 30:
                if find_repeat(square) == 1:
                    return 1
    return 0


# get user input and return 2d array
def getuserinput():
    square = []
    i = 1
    for x in range(N):
        row_list = []
        for y in range(N):
            print("Enter number", i, "[", x, "][", y, "]: ", end="")
            row_list.append(int(input(), 10))
            i += 1
        square.append(row_list)
    return square


def check_square(square):
    if check_equal(sum_horizontal(square)) and check_equal(sum_vertical(square)) and check_equal(sum_diagonals(square)):
        is_magic = 1
    else:
        is_magic = 0

    if is_lo_shu(square):
        is_loshu = 1
    else:
        is_loshu = 0

    if is_magic and is_loshu:
        print("Square is Magic and is Lo Shu\n")
        return
    elif is_magic and not is_loshu:
        print("Square is Magic, but not Lo Shu\n")
        return
    elif not is_magic:
        print("Square is not Magic\n")
        return


def main():
    while 1:
        square = getuserinput()
        check_square(square)
        repeat = input('Do you wish to enter an new square? (y/n)')
        if "n" in repeat:
            break
    print("Bye!")


main()
