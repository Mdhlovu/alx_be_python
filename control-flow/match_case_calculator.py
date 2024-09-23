first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

case_operation = input("Choose the operation (+, -, *, /): ")

match case_operation:

    case "+":
         results = first_number + second_number
         print(f"The results is {results}")

    case "-":
         results = first_number - second_number
         print(f"The results is {results}")

    case "*":
         results("The results is {results}")
         print(f"The results is {results}")

    case "/":
        if second_number != 0:
             results = first_number / second_number
             print(f"The results is {results}")

        else:
             print(f"Cannot divide by zero.")
    case _:
             print(f"Invalid")



