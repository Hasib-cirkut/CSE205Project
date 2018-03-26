
m = int(input("Enter m(Mod Value): "))
a = int(input("Enter a(Multiplier Value): "))
c = int(input("Enter c(Increment Value): "))
x = int(input("Enter x(Seed): "))

dataSet = []

Ans = -1
l = x

def mod(a, b):
    rem = a % b
    
    if rem < 0:
        if b < 0:
            rem = rem - b
        else:
            rem = rem + b

    return rem

i = 0
while True:
    i += 1
    temp = (a * l + c)
    Ans = mod(temp, m)
    l = Ans
    if(Ans == x):
        break
    dataSet.append(Ans)
    #print("x", i, "= ", Ans)


dataSet = [str(i) for i in dataSet] #List comprehension

resultString = ' '.join(dataSet)

print('\n\n',resultString, "\n\n")
print("Total", i-1, "values generated")





