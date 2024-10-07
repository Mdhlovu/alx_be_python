def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"Success: {numerator} divided by {denominator} equals {result}"

    except ZeroDivisionError:
        return "Error:  can't divide by zero."

    except ValueError:
        return "Error: Please enter valid numbers."


