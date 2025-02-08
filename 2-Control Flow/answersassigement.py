# #question 1

# usernumber = int(input("please Enter a number: "))
# if usernumber >0:
#     print("The number is positive")
# else:
#     print("The number is negative")

# #question 2
# usernumber = int(input("please Enter a number: "))

# if usernumber > 0:
#     print("The number is positive")
# elif usernumber < 0:
#     print("The number is negative")
# else:
#     print("The number is zero")

# #question 3
# for i in range(1,11):
#     print(i)

# #question 4

num =0
while num < 11:
    print(num)
    num += 1

#another way

num = 11

count = 0

while count < num:
    print(count)
    count += 1

# Print a 5x5 grid of asterisks
for i in range(5):
    for j in range(5):
        print('*', end=' ')  # end=' ' adds a space after each asterisk
    print()  # print() creates a new line after each row

# Print a half triangle of asterisks
for i in range(5):
    for j in range(i + 1):
        print('*', end=' ')
    print()

    # Print a full triangle (pyramid) of asterisks
n = 5  # height of the pyramid
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(' ', end=' ')
    # Print asterisks
    for k in range(2 * i + 1):
        print('*', end=' ')
    print()

# Print a diamond of asterisks
n = 5  # height of the diamond
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(' ', end=' ')
    # Print asterisks
    for k in range(2 * i + 1):
        print('*', end=' ')
    print()    
    def print_grid(size=5):
        print("\n=== Square Grid Pattern ===")
        for i in range(size):
            for j in range(size):
                print('*', end=' ')
            print()
    
    def print_half_triangle(size=5):
        print("\n=== Half Triangle Pattern ===")
        for i in range(size):
            print('* ' * (i + 1))
    
    def print_pyramid(size=5):
        print("\n=== Pyramid Pattern ===")
        for i in range(size):
            spaces = ' ' * (size - i - 1)
            stars = '* ' * (2 * i + 1)
            print(spaces + stars)
    
    def print_diamond(size=5):
        print("\n=== Diamond Pattern ===")
        # Upper half
        for i in range(size):
            spaces = ' ' * (size - i - 1)
            stars = '* ' * (2 * i + 1)
            print(spaces + stars)
        # Lower half
        for i in range(size-2, -1, -1):
            spaces = ' ' * (size - i - 1)
            stars = '* ' * (2 * i + 1)
            print(spaces + stars)
    
    def print_heart():
        print("\n=== Heart Pattern ===")
        for i in range(6):
            for j in range(7):
                if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
    
    def print_butterfly(size=4):
        print("\n=== Butterfly Pattern ===")
        # Upper half
        for i in range(size):
            print('* ' * (i + 1) + '  ' * (2*(size-i-1)) + '* ' * (i + 1))
        # Lower half
        for i in range(size-1, -1, -1):
            print('* ' * (i + 1) + '  ' * (2*(size-i-1)) + '* ' * (i + 1))
    
    # Main execution
    if __name__ == "__main__":
        size = 5  # Default size for patterns
        print_grid(size)
        print_half_triangle(size)
        print_pyramid(size)
        print_diamond(size)
        print_heart()
        print_butterfly(4)


#assignment 11

number = int(input("Enter a number: "))
for i in range(1, number):
    if number % 2 == 0:
        print(i)
