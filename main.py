# main.py
from calculator import calculate

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Choose operation (add, subtract, multiply, divide): ")

        result = calculate(a, b, operation)
        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
