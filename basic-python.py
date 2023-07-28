

def add (a, b) : 
    return a + b

def div (a, b ): 
    return a / b

def multi(a, b): 
    return a * b

def subtract(a, b):
    return a - b


firstNum = int(input("첫번째 숫자를 입력해주세요"))
specialText = input()
secondNum = int(input("두번째 숫자를 입력해주세요"))

while(True) : 
    if(specialText == "+") : 
        text = f"{firstNum} + {secondNum} = {add(firstNum,secondNum)}"
        print(text)
        break

    if(specialText == "-") : 
        text = f"{firstNum} + {secondNum} = {subtract(firstNum,secondNum)}"
        print("12321321")
        print(text)
        break

    if(specialText == "*") : 
        text = f"{firstNum} * {secondNum} = {multi(firstNum,secondNum)}"
        print(text)
        break

    if(specialText == "/") : 
        text = f"{firstNum} / {secondNum} = {div(firstNum,secondNum)}"
        print(text)
        break

    else:
        print("잘못된 입력")
        break