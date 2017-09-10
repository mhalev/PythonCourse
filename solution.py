import sys

try:
    int(sys.argv[1])
except ValueError:
    print("В качестве параметра должно быть задано число. Это похоже на число: " + sys.argv[1] + " ?")
else:
    digit_string = sys.argv[1]
    result = 0
    for i in range(len(sys.argv[1])):
        result += int(digit_string[i])
    print("Сумма чисел в параметре: " + str(result))
