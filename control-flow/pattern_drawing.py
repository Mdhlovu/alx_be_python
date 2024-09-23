size = -1
while size <= 0:
    size = input("Enter the size of the pattern: ")

    if size:  
        valid = True  
        for i in range(len(size)):
            if size[i] < '0' or size[i] > '9':
                valid = False
                break

        if valid: 
            size = int(size)  
            if size <= 0:
                print("Please enter a positive integer.")
        else:
            print("Invalid input. Please enter a positive integer.")
            size = -1
    else:
        print("Invalid input. Please enter a positive integer.")
        size = -1

row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print() 
    row += 1
