num1 = float(input("Digite o primeiro valor!"))
num2 = float(input("Digite o segundo valor!"))
num3 = float(input("Digite o terceiro valor!"))

if num1<num2 and num1<num3:
    print(num1)
elif num2<num1 and num2<num3:
    print(num2)
else:
    print(num3)

if (num2>num3 and num2>num1) and num3>num1:
    print(num3)
elif (num2>num3 and num2>num1) and num3<num1:
    print(num1)
elif(num2<num3 and num2<num1) and num3<num1:
    print(num3)
elif(num2<num3 and num2<num3) and num3<num1:
    print(num3)
else:
    print(num2)

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)
