def is_valid(n):
    return n % 2 != 0 and n > 0


def create_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    i = n // 2
    j = n - 1
    num = 1

    while num <= n * n:
        if i == -1 and j == n:
            i = 0
            j = n - 2
        else:
            if i < 0:
                i = n - 1
            if j == n:
                j = 0

        if magic_square[i][j]:
            i += 1
            j -= 2
            continue
        else:
            magic_square[i][j] = num
            num += 1

        i -= 1
        j += 1

    return magic_square


def print_magic_square(magic_square):
    n = len(magic_square)
    for i in range(n):
        for j in range(n):
            print(f"{magic_square[i][j]:3}", end=" ")
        print()


def verify_magic_square(magic_square):
    n = len(magic_square)
    magic_sum = n * (n ** 2 + 1) // 2

    # Verify rows
    for i in range(n):
        row_sum = sum(magic_square[i])
        if row_sum != magic_sum:
            return False

    # Verify columns
    for j in range(n):
        col_sum = sum(magic_square[i][j] for i in range(n))
        if col_sum != magic_sum:
            return False

    # Verify diagonals
    main_diag_sum = sum(magic_square[i][i] for i in range(n))
    anti_diag_sum = sum(magic_square[i][n - i - 1] for i in range(n))
    if main_diag_sum != magic_sum or anti_diag_sum != magic_sum:
        return False

    return True


def main():
    n = int(input("Enter a positive odd integer (N): "))

    while not is_valid(n):
        print("Invalid input! N must be a positive odd integer.")
        n = int(input("Enter a positive odd integer (N): "))

    magic_square = create_magic_square(n)
    print("Magic Square:")
    print_magic_square(magic_square)

    if verify_magic_square(magic_square):
        print("Correct! The magic square is valid.")
    else:
        print("The magic square is not valid.")


if __name__ == "__main__":
    main()
