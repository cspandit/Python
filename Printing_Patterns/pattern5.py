# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def print_pat(n):
    count = 1
    for i in range(n):
        for j in range(i+1):
            print(count, end=' ')
            count += 1
        print('\n', end='')


print_pat(5)