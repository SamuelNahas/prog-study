def validateGrade():
    while True:
        number = float(input())
        if 0 <= number <= 10:
            return number
        else:
            print("nota invalida")

while True:        

    userNumber1 = validateGrade()
    userNumber2 = validateGrade()

    average = (userNumber1 + userNumber2) / 2

    print("media = ", average)

    newCalculation = input("novo calculo (1-sim 2-nao)\n")
    
    while newCalculation != "1" and newCalculation != "2":
        newCalculation = input("novo calculo (1-sim 2-nao)\n")
    if newCalculation == "2":
        break
    


