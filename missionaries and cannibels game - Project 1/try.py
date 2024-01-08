try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError as ve:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError as zde:
    print("Error: Division by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
