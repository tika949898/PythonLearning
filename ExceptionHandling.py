def divide_numbers(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
        result=None
    except TypeError as e:
        print(f"Error:{e}")
        result=None
    else:
        print("Division successful!")
    finally:
        print("This will  always be executed, whether there was an exception or not.")
        return result
# Example:
result1=divide_numbers(10,2)
print("Result 1:", result1)
result2=divide_numbers(10,0)
print("Result 2:", result2)
result3=divide_numbers("10",2)
print("Result 3:",result3)