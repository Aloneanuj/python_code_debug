'''
      1 
    1 2 3 
  1 2 3 4 5
1 2 3 4 5 6 7
  1 2 3 4 5
    1 2 3
      1

'''
def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()


pattern(7)