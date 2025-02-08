# age = 20

# if age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a child")

    #loops in python
    # for loop
for i in range (1,10,3):
        print(i)
# while loop
for i in range (10,1,-1):
        print(i)

str ="this is random text"

for i in str:
    print(i)

#while loop
count = 0

while count < 10:
    print(count)
    count += 1

#break and continue statements
for i in range(10):
    if i == 5:
        break
    print(i)


#prime number between 1 and 100

for num in range(1,101):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)