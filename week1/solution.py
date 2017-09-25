import sys

if not sys.argv[1].isdigit():
    print("В качестве параметра должно быть задано число. Это похоже на число: " + sys.argv[1] + " ?")
else:
    digit_string = sys.argv[1]
    result = 0
    for i in digit_string:
        result += int(i)
    print("Сумма чисел в параметре: " + str(result))
