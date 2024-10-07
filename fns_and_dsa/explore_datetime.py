import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date:%Y-%m-%d %H:%M:%S}")

def calculate_future_date():
    days = input("Enter the number of days to add to the current date: ")
    
    if days.isdigit():
        days = int(days)
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(days=days)
        print(f"Future date: {future_date:%Y-%m-%d}")
    else:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

