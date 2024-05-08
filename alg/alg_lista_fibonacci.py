def fibonacci(number):
    p1 = 0
    p2 = 1

    if number == 2: cont = 0
    cont = 2
    

    while cont <= number:
        if cont == 2 or number == 1:
            print('1', end='')

        fibonacci = p1 + p2
        print(", {0}".format(fibonacci), end= '')
        p1 = p2
        p2 = fibonacci
        cont += 1

numb = int(input())

if numb < 1:
    print("0")
if numb == 1:
    print("1")

else:
    fibonacci(numb)