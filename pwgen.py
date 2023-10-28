import random

def pwRandom(size, specChar):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    specialChar = "!@#$%^&*()"

    arr = []
    i = 0
    while(i < size):
        ranChar = random.randint(0, len(specialChar)-1)
        ranLetter = random.randint(0, len(letters)-1)
        ranNum = random.randint(0, len(numbers)-1)
        if specChar == True:
            if i % 3 == 0:
                arr.append(letters[ranLetter])
            elif i % 3 == 1:
                arr.append(numbers[ranNum])
            else:
                arr.append(specialChar[ranChar])
        else:
            if i % 2 == 0:
                arr.append(letters[ranLetter])
            else:
                arr.append(numbers[ranNum])
        i += 1

    return ''.join(arr)

def userName(first, last):
    numbers = "1234567890"
    
    arr = []

    arr.append(first)
    arr.append(last)

    i = 0
    while(i < 4):  
        ranNum = random.randint(0, len(numbers)-1)
        arr.append(numbers[ranNum])
        i += 1

    return ''.join(arr)

def main():
    # print(userName("Khoi", "Pham",))
    print(pwRandom(5, False))
    
if __name__ == '__main__':
    main()
    