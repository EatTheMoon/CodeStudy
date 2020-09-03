def compare(opt1,opt2):
    return opt1 in ["x","/"] and opt2 in ["+","-"]

def getvalue(num1,num2,opt):
    if opt == "+":
        return num1+num2
    if opt == "-":
        return num1-num2
    if opt == "x":
        return num1*num2
    if opt == "/":
        return num1/num2


def process(data, opt):
    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(getvalue(int(num1),int(num2),operator))


def calculate(s):
    data = []
    opt = []
    i = 0
    while i<len(s):
        if s[i].isdigit(): 
            data.append(s[i])

        elif not opt or compare(s[i],opt[-1]):
            opt.append(s[i])

        else:
            while opt and not compare(s[i],opt[-1]):
                process(data,opt)
            opt.append(s[i])
        i += 1
    while opt:
        process(data,opt)
    if data.pop() - 24 == 0:
        return "Yes"
    else:
        return "No"

n = int(input())
ans = []
for i in range(n):
    string = input()
    ans.append(calculate(string))

for i in ans:
    print(i)
