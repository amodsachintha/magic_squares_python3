# https://github.com/amodsachintha/magic_squares_python3

# Array dimensions
N = 3

# Directions
HORIZONTAL = "HORIZONTAL"
VERTICAL = "VERTICAL"
DIAGONAL = "DIAGONAL"

# use this array to bypass user input when testing
SQUARE = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 6]]


# Horizontal, Vertical and Diagonal summing
def universal_sum(square, direction):
    diagonal_1 = 0
    diagonal_2 = 0
    row_sum = 0
    u_sum = []
    for x in range(N):
        if direction == DIAGONAL:
            diagonal_1 += square[x][x]
            diagonal_2 += square[x][N - (x + 1)]
        for y in range(N):
            if direction == HORIZONTAL:
                row_sum += square[x][y]
            elif direction == VERTICAL:
                row_sum += square[y][x]
        u_sum.append(row_sum)
        row_sum = 0
    if direction == DIAGONAL:
        return [diagonal_1, diagonal_2]
    return u_sum


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
    for row in square:
        for element in row:
                if element >= 10:
                    return 0

    if sum(universal_sum(square, HORIZONTAL)) == 45:
        if sum(universal_sum(square, VERTICAL)) == 45:
            if sum(universal_sum(square, DIAGONAL)) == 30:
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
    if check_equal(universal_sum(square, HORIZONTAL)) and check_equal(universal_sum(square, VERTICAL)) and check_equal(
            universal_sum(square, DIAGONAL)):
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
        repeat = input('Do you wish to enter a new square? (y/n)')
        if "n" in repeat:
            break
    print("Bye!")


main()
