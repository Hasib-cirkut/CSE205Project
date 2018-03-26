def mod(a, b):
    rem = a%b

    if rem < 0:
        if b < 0:
            rem = rem + b
        else:
            rem = rem - b
        

    return rem

def encript(data, result):
    key = int(input("Enter your key: "))
    modVal = int(input("Enter your mod value: "))

    for i in range(len(data)):
        dataValint = ord(data[i]) #ord is func that turns charcters to unicode

        if dataValint == 32 : #32 is ascii code for space
            result.append((mod(26 + key, modVal)))
        else :
            dataValint -= 65 #To make them A=0, B=1, C=2 etc...
            result.append((mod((dataValint + key), modVal))) #Appending every result to a list
    
    
    
    for i in range(len(result)):
        result[i] = result[i] + 65 #Adding 65 to transform them back to characters

    result = [chr(c) for c in result] #Transforming unicodes back to character using list comprehension
        
    resultStr = ''.join(result) #Turning list to a string using join. Ex:>> a = ['1','2','3'] 
                                                                      #  >> string = ''.join(a)
                                                                      #  >> string
                                                                      #  >> '123'

    print(resultStr)

    
    choice = int(input("Press 1 to dycript current cipher\nPress 2 to return to main menu\n"))

    if choice ==  1:
        del result[:]
        dycript(resultStr, result)
    elif choice == 2:
        return

def dycript(data, result):
    key = int(input("Enter your key: "))
    modVal = int(input("Enter your mod value: "))

    for i in range(len(data)):
        dataValint = ord(data[i])

        
        dataValint -= 65 #To make them A=0, B=1, C=2 etc...
            
        result.append((mod((dataValint - key), modVal)))

    for i in range(len(result)):
        if result[i] == 26: #If it is space then change it to space's unicode which is 32
            result[i] = 32
        else:
            result[i] += 65 #Adding 65 so that we can turn them back to characters from unicode
    
    result = [chr(c) for c in result] #List comprehension. It is similler to,
                                                            # for i in range(len(result)):
                                                            #   temp = chr(result[i])
                                                            #   result[i] = temp    

    resultStr = ''.join(result)

    print(resultStr)
            
    
    input("Press enter for main menu..\n")

while True:
    result = []
    print("Enter 1 to input message\nEnter 0 to exit\n")
    ch = int(input())
    if ch == 1:
        MainStr = (str(input("Enter your message: "))).upper()    
        print("Enter 1 to encrypt\nEnter 2 to dycript\n")
        choice = int(input())
        if choice == 1 :
            encript(MainStr, result)
        elif choice == 2 :
            dycript(MainStr, result)
    
    elif ch == 0:
        break;